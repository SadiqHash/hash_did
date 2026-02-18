from hash_did.engine.zk import generate_challenge


def test_challenge():
    challenge = generate_challenge()
    assert len(challenge) == 32
