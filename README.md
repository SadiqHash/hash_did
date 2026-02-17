Hash DID

Offline-first decentralized identity engine for normal humans.

---

What is Hash DID?

Hash DID is a portable identity engine that allows individuals to create, own, and use decentralized identities without relying on centralized databases or mandatory blockchain infrastructure.

It is:

* Offline-first
* Privacy focused
* Lightweight
* Designed for low-end devices
* Installable as a CLI tool
* Optional API enabled

Hash DID is not a SaaS platform.
It is not a cloud identity provider.
It is not tied to any blockchain.

It is a local identity engine that runs on your machine and gives users full control over:

* Their Decentralized Identifiers (DIDs)
* Their private keys
* Their Verifiable Credentials
* Their authentication proofs

Hash DID separates:

* Identity logic (engine)
* Local wallet storage
* CLI interface
* API interface

The core engine works independently of any web server.

---

Why Hash DID Exists?

Most identity systems today are:

* Centralized
* Password based
* Dependent on remote servers
* Vulnerable to data breaches
* Not portable

Even many decentralized identity solutions:

* Require blockchain
* Require internet
* Require heavy infrastructure
* Are too complex for normal users

Hash DID exists to solve a different problem:

How can a normal person own their identity securely, even without internet?

It is designed for:

* Low connectivity environments
* Privacy sensitive use cases
* Regions with unstable infrastructure
* Students and researchers experimenting with DID systems
* Developers building identity aware applications

Hash DID focuses on:

* Cryptographic ownership (Ed25519 keys)
* Portable encrypted wallet backups
* Password derived key encryption (Argon2 + AES-256-GCM)
* Optional zero-knowledge authentication
* QR-based identity exchange

No blockchain dependency. No centralized authority. No required internet connection.

---

How Hash DID Works Offline

This is the most important concept.

Hash DID is built around a local identity wallet.

Architecture:

```
Local Wallet (SQLite + Encrypted JSON)
        |
        v
Hash DID Engine
        |
        ├── DID Manager
        ├── Credential Engine
        ├── ZK Proof Module
        └── QR Sharing Module
```

---

Offline Identity Creation

When you create a DID:


1. keypair is generated (Ed25519).


2. Public key is hashed.


3. DID is formed:

```
did:hash:<public-key-hash>
```

4. A DID Document is generated locally.


5. Private key is encrypted using:

  * Password derived key (Argon2)
  * AES-256-GCM encryption


6. Stored inside local wallet.

No network request is made.

---

Offline Credential Verification

When verifying a credential:


1. Credential JSON is loaded locally.


2. Issuer signature is verified.


3. Public key is resolved from DID document.


4. Validation is performed locally.

No blockchain lookup. No centralized registry.

---

Offline Authentication (ZK Login)

Zero-knowledge login works by:


1. Generating a challenge.


2. Signing proof locally.


3. Verifier checks signature.


This can be done over:

* Local network
* QR code
* Direct device-to-device exchange

Internet is optional.

---

Backup & Portability

Wallets can be exported as:

* Encrypted JSON file
* QR-encoded encrypted payload

If device dies:

  * Identity can be restored with password + backup.

Ownership stays with the user.

---

How Developers, Students & Researchers Can Use Hash DID

Hash DID is built to be used in two ways:


1. CLI (local tool)


2. API (backend integration)


Both use the same engine.


Installation

Using Poetry:

```bash
poetry install
```

Install with API support:

```bash
poetry install --with api
```

Or pip (when published):

```bash
pip install hash_did
pip install hash_did[api]
```

---

Using Hash DID via CLI

Entry point:

```bash
hash-did
```

Initialize Wallet

```bash
hash-did wallet init
```

Create DID

```bash
hash-did did create
```

Resolve DID

```bash
hash-did did resolve did:hash:abc123
```

Issue Credential

```bash
hash-did credentials issue \
    --issuer did:hash:gov123 \
    --subject did:hash:user456 \
    --claims '{"name":"Sadiq","age":25}'
```

Verify Credential

```bash
hash-did credentials verify credential.json
```

Generate ZK Login Proof

```bash
hash-did proof generate --did did:hash:user456
```

The CLI is ideal for:

* Students learning DID systems
* Offline demos
* Identity experimentation
* Security research

---

Using Hash DID via API

Start server:

```bash
uvicorn hash_did.interfaces.api.main:app --reload
```

Example: Create DID

```bash
POST /api/v1/did/create
```

Example: Issue Credential

```bash
POST /api/v1/credentials/issue
```

Example: Verify Credential

```bash
POST /api/v1/credentials/verify
```

This is useful for:

* Backend developers integrating identity
* Research prototypes
* Educational labs
* Web or mobile apps

---

Using Hash DID as a Library

You can also import the engine directly:

```python
from hash_did.engine.did.manager import DIDManager
from hash_did.engine.crypto.keys import generate_keypair

manager = DIDManager()
did = manager.create()
print(did)
```

This makes Hash DID:

* Research-friendly
* Framework-agnostic
* Extensible

---

Security Principles

Hash DID follows:

* Key ownership over account ownership
* Encryption at rest
* Minimal attack surface
* No mandatory remote calls
* Deterministic cryptographic identity

It is an experimental identity engine and should be audited before production deployment.

---

License & Contribution

License

Hash DID is released under the MIT License.

See LICENSE for full details.

---

Contributing

We welcome:

* Security reviews
* Cryptographic feedback
* DID format suggestions
* Educational improvements
* Documentation contributions

Before contributing:


1.  Fork repository


2. Create feature branch


3. Ensure:

  * Tests pass
  * Code is typed
  * Lint passes


4. Open Pull Request

For major architectural changes, open an issue first to discuss design impact.

---

Final Note


Hash DID is built around a simple idea:

  * Identity should belong to people, not servers.

This project aims to make decentralized identity understandable, portable, and practical.
