class TrustedRetrievalGuard:
    """
    Defends against LLM09 Vector & Embedding Weaknesses (Day 10's exploit).
    Documents from a trusted source are indexed immediately.
    Anything else goes into quarantine and is NEVER returned to a user,
    no matter how well it scores on similarity, until explicitly approved.
    """

    TRUSTED_SOURCES = {"official_docs_team"}

    def __init__(self):
        self.trusted_index = []
        self.quarantine = []

    def ingest(self, document: str, source: str) -> dict:
        if source in self.TRUSTED_SOURCES:
            self.trusted_index.append(document)
            return {"status": "indexed", "trusted": True}
        self.quarantine.append({"document": document, "source": source})
        return {"status": "quarantined", "trusted": False, "note": "Requires review before retrievable"}

    def _score(self, query: str, doc: str) -> float:
        q_words = set(query.lower().split())
        d_words = set(doc.lower().split())
        if not q_words or not d_words:
            return 0.0
        return len(q_words & d_words) / len(q_words)

    def query(self, user_query: str) -> dict:
        # ONLY searches trusted_index - quarantined documents are structurally
        # excluded from ever being a candidate, regardless of similarity score
        if not self.trusted_index:
            return {"response": "No documents indexed yet."}
        scored = [(self._score(user_query, d), d) for d in self.trusted_index]
        scored.sort(key=lambda x: x[0], reverse=True)
        top_score, top_doc = scored[0]
        if top_score == 0:
            return {"response": "No relevant document found."}
        return {"response": top_doc, "match_score": top_score}
        