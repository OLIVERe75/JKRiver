
from datetime import datetime, date
from flask import Blueprint, jsonify, request
from psycopg2.extras import RealDictCursor
from web._helpers import get_conn, _serialize

observations_bp = Blueprint("observations", __name__)


@observations_bp.route("/api/observations")
def api_observations():
    obs_type = request.args.get("type")
    conn = get_conn()
    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        conditions = []
        params = []
        if obs_type:
            conditions.append("observation_type = %s")
            params.append(obs_type)
        where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        cur.execute(
            f"SELECT id, session_id, observation_type, content, subject, context, created_at, "
            f"rejected, note "
            f"FROM observations {where} "
            f"ORDER BY rejected ASC, created_at DESC",
            params,
        )
        rows = cur.fetchall()
        return jsonify([{k: _serialize(v) if isinstance(v, (datetime, date)) else v
                         for k, v in row.items()} for row in rows])
    finally:
        conn.close()
