_CATEGORY_SYNONYM_GROUPS = [
    {"位置", "居住地", "居住城市", "地点", "住址", "居住", "所在地",
     "location", "residence"},
    {"职业", "职位", "工作", "岗位",
     "career", "work", "job", "仕事"},
    {"教育", "教育背景", "学历",
     "education", "教育背景"},
    {"家乡", "籍贯", "出生地", "老家",
     "hometown", "birthplace"},
    {"兴趣", "爱好", "休闲活动", "休闲", "运动", "运动与锻炼",
     "hobby", "interest", "sports", "趣味"},
    {"感情", "恋爱", "情感", "婚恋",
     "relationship", "romance"},
    {"出生年份", "年龄", "出生年",
     "age", "birth_year"},
    {"专业", "学科", "主修",
     "major", "subject"},
    {"娱乐", "游戏",
     "entertainment", "gaming"},
    {"宠物", "养宠",
     "pet", "pets", "ペット"},
    {"技能", "技术", "编程",
     "skills", "tech", "programming"},
    {"身份", "个人信息",
     "identity", "personal_info"},
    {"饮食", "饮食与美食", "美食",
     "diet", "food", "cuisine"},
    {"家庭", "家人",
     "family", "家族"},
    {"健康", "health", "健康状態"},
    {"健身", "fitness", "フィットネス"},
    {"旅行", "出行", "travel", "旅行"},
]

_CAT_SYNONYM_MAP: dict[str, set[str]] = {}
for _group in _CATEGORY_SYNONYM_GROUPS:
    for _name in _group:
        _CAT_SYNONYM_MAP[_name] = _group

_SUBJECT_SYNONYM_GROUPS = [
    {"居住地", "居住城市", "当前居住地", "所在城市"},
    {"职业", "当前职位", "工作", "职位", "岗位"},
    {"学校", "大学", "毕业学校"},
    {"专业", "主修", "学科"},
    {"家乡", "老家", "出生地"},
    {"运动", "体育", "锻炼"},
    {"游戏", "电子游戏"},
    {"出生年", "出生年份"},
    {"女朋友", "女友", "对象"},
    {"男朋友", "男友"},
]

_SUBJ_SYNONYM_MAP: dict[str, set[str]] = {}
for _group in _SUBJECT_SYNONYM_GROUPS:
    for _name in _group:
        _SUBJ_SYNONYM_MAP[_name] = _group

def _get_category_synonyms(category: str) -> set[str]:
    return _CAT_SYNONYM_MAP.get(category, {category})

def _get_subject_synonyms(subject: str) -> set[str]:
    return _SUBJ_SYNONYM_MAP.get(subject, {subject})


# ── Significant-category check ──────────────────────────
# Categories where a change should trigger earlier trajectory updates.
# One anchor per group; expanded at import time via synonym map.

_SIGNIFICANT_CATEGORY_ANCHORS = frozenset({
    "职业", "家庭", "居住", "教育", "健康",
})

_SIGNIFICANT_CATEGORIES: set[str] = set()
for _anchor in _SIGNIFICANT_CATEGORY_ANCHORS:
    _SIGNIFICANT_CATEGORIES |= _CAT_SYNONYM_MAP.get(_anchor, {_anchor})

def is_significant_category(category: str) -> bool:
    """Check if a category is 'significant' (career, family, location, etc.)."""
    return category in _SIGNIFICANT_CATEGORIES or category.lower() in _SIGNIFICANT_CATEGORIES
