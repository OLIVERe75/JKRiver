
from datetime import datetime, date
from flask import Blueprint, jsonify, request
from psycopg2.extras import RealDictCursor
from web._helpers import get_conn, _serialize

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/api/profile")
def api_profile():
    category = request.args.get("category")
    conn = get_conn()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        conditions = ["end_time IS NULL"]
        params = []
        if category:
            conditions.append("category = %s")
            params.append(category)
        where = "WHERE " + " AND ".join(conditions)
        cur.execute(
            f"SELECT id, category, subject, value, layer, source_type, "
            f"start_time, decay_days, expires_at, evidence, mention_count, "
            f"created_at, updated_at, confirmed_at, superseded_by, supersedes, "
            f"rejected, human_end_time, note "
            f"FROM user_profile {where} "
            f"ORDER BY rejected ASC, "
            f"CASE layer WHEN 'confirmed' THEN 1 WHEN 'suspected' THEN 2 END, "
            f"category, subject",
            params,
        )
        rows = cur.fetchall()
        return jsonify([{k: _serialize(v) if isinstance(v, (datetime, date)) else v
                         for k, v in row.items()} for row in rows])
    finally:
        conn.close()


@profile_bp.route("/api/timeline")
def api_timeline():
    category = request.args.get("category")
    conn = get_conn()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        conditions = []
        params = []
        if category:
            conditions.append("category = %s")
            params.append(category)
        where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        cur.execute(
            f"SELECT id, category, subject, value, layer, source_type, "
            f"start_time, end_time, mention_count, superseded_by, supersedes, "
            f"rejected, human_end_time, note "
            f"FROM user_profile {where} "
            f"ORDER BY category, subject, start_time",
            params,
        )
        rows = cur.fetchall()
        return jsonify([{k: _serialize(v) if isinstance(v, (datetime, date)) else v
                         for k, v in row.items()} for row in rows])
    finally:
        conn.close()


@profile_bp.route("/api/relationships")
def api_relationships():
    conn = get_conn()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "SELECT id, name, relation, details, mention_count, "
            "first_mentioned_at, last_mentioned_at "
            "FROM relationships WHERE status = 'active' "
            "ORDER BY last_mentioned_at DESC"
        )
        rows = cur.fetchall()
        return jsonify([{k: _serialize(v) if isinstance(v, (datetime, date)) else v
                         for k, v in row.items()} for row in rows])
    finally:
        conn.close()


@profile_bp.route("/api/trajectory")
def api_trajectory():
    conn = get_conn()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM trajectory_summary ORDER BY updated_at DESC LIMIT 1")
        row = cur.fetchone()
        if row:
            return jsonify({k: _serialize(v) if isinstance(v, (datetime, date)) else v
                            for k, v in row.items()})
        return jsonify(None)
    finally:
        conn.close()
