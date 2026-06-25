from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Scanrequest(BaseModel):
    repo_url: str
    branch: Optional[str] = "main"


class AnalyzeRequest(BaseModel):
    code: str
    langage: Optional[str] = "python"


class Issue(BaseModel):
    line: int
    message: str
    severity: str
    category: Optional[str] = None
    code_snippet: Optional[str] = None


class ScanResponse(BaseModel):
    scan_id: str
    status: str
    message: str


class ScanStatusResponse(BaseModel):
    scan_id: int
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    total_issues: Optional[int] = None
    issues: Optional[List[Issue]] = None
    error: Optional[str] = None


class AnalyzeResponse(BaseModel):
    issues: List[Issue]
    total_issues: int
    status: str
