"""Favro share-link handling shared by resolvers keyed on a /widget/<org>/<id> URL.

Both cards and boards can be shared as favro.com/widget/<org>/<id>?secret=... links.
The secret token is a web-only view bypass the REST API doesn't recognize, so it
carries no meaning to us here.
"""

import re

# Toggle whether pasted Favro share links are stripped down to the bare ID before
# resolution.
STRIP_SHARE_LINK_TOKENS = True

_SHARE_LINK_RE = re.compile(
    r"^https?://favro\.com/widget/[0-9a-fA-F]+/([0-9a-fA-F]+)(?:\?.*)?$"
)


def strip_share_link(identifier: str) -> str:
    """Extract the bare ID from a Favro widget share link, if present."""
    if not STRIP_SHARE_LINK_TOKENS:
        return identifier
    match = _SHARE_LINK_RE.match(identifier.strip())
    return match.group(1) if match else identifier
