class MultiTokenSpeculativeFimCodeGeneratorClient:
    def complete_fill_in_the_middle(self, prefix_context='def calculate_sha256_tree(nodes: list[bytes]) -> bytes:\n    if not nodes:\n        return b""\n', suffix_context='\n    return nodes[0]\n', target_language='PYTHON'):
        return {
            'completion_job_id': 'fim_gen_8812',
            'language': target_language,
            'speculative_draft_tokens_accepted': 42,
            'acceptance_rate_pct': 88.5,
            'synthesized_middle_code': '    while len(nodes) > 1:\n        nodes = [hashlib.sha256(nodes[i] + (nodes[i+1] if i+1 < len(nodes) else nodes[i])).digest() for i in range(0, len(nodes), 2)]',
            'ast_syntax_verified': True,
            'latency_ms': 28
        }
