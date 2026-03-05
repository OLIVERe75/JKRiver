-- Migration: Add pgvector support for memory_embeddings
-- Prerequisites: PostgreSQL with pgvector extension installed
--   brew install pgvector  (macOS)
--   apt install postgresql-16-pgvector  (Debian/Ubuntu)
--
-- This migration is safe to run multiple times (idempotent).
-- The application code auto-detects pgvector availability and falls back
-- to JSONB+Python if the extension is not installed.

-- 1. Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Add vector column (preserving original JSONB column for rollback)
ALTER TABLE memory_embeddings
    ADD COLUMN IF NOT EXISTS embedding_vec vector(1024);

-- 3. Migrate existing JSONB embeddings to vector column
UPDATE memory_embeddings
SET embedding_vec = embedding::text::vector
WHERE embedding_vec IS NULL
  AND embedding IS NOT NULL;

-- 4. Create IVFFlat index for fast approximate nearest neighbor search
-- Note: IVFFlat requires at least `lists` rows to be effective.
-- For small datasets (<1000 rows), this still works but HNSW may be better.
CREATE INDEX IF NOT EXISTS idx_memory_embeddings_vec
    ON memory_embeddings USING ivfflat (embedding_vec vector_cosine_ops)
    WITH (lists = 100);
