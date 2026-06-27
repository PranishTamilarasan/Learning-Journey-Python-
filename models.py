from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Issue:
    line: int
    message: str
    severity: str
    category: Optional[str] = None
    code_snippet: Optional[str] = None


@dataclass
class Scan:
    id: int
    repo_url: str
    branch: str
    status: str  # queued, cloning, analyzing, completed, failed
    created_at: datetime
    completed_at: Optional[datetime] = None
    total_issues: int = 0
    issues: List[Issue] = field(default_factory=list)
    error: Optional[str] = None


scan_db = Dict[int, Scan] = {}
scan_counter = 1
