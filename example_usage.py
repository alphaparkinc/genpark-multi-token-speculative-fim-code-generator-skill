from client import MultiTokenSpeculativeFimCodeGeneratorClient

def main():
    client = MultiTokenSpeculativeFimCodeGeneratorClient()
    res = client.complete_fill_in_the_middle('async function fetchBatch(ids) {', 'return results; }', 'TYPESCRIPT')
    print('Speculative FIM Job: ' + res['completion_job_id'] + ' (Language: ' + res['language'] + ')')
    print('Speculative Tokens Accepted: ' + str(res['speculative_draft_tokens_accepted']) + ' (Acceptance Rate: ' + str(res['acceptance_rate_pct']) + '%)')
    print('AST Syntax Verified: ' + str(res['ast_syntax_verified']) + ' in ' + str(res['latency_ms']) + 'ms')
    print('Synthesized Middle:\n' + res['synthesized_middle_code'])

if __name__ == '__main__':
    main()
