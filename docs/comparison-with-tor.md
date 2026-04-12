#How Similar Is It to Tor?

Very similar in concept.But there are real differences.

## The Short Version

PrivacyNet Lab and Tor share the same **underlying theory** — onion
routing and layered encryption. But they are built for completely
different purposes. Tor is a production anonymity network. PrivacyNet
Lab is a transparent educational tool that makes those same concepts
visible and understandable.

---

## Side-by-Side Comparison

| Feature                  | Tor                                      | PrivacyNet Lab                          |
|--------------------------|------------------------------------------|-----------------------------------------|
| Core concept             | Onion routing                            | Onion routing (same)                    |
| Encryption per hop       | ✅ AES layered encryption                | ✅ AES-256 layered encryption           |
| Number of hops           | 3 (guard, middle, exit)                  | 3 (entry, middle, exit)                 |
| Node isolation           | ✅ Each node sees only neighbours        | ✅ Same design principle                |
| Network type             | Public — thousands of global nodes       | Private — your machines only            |
| Anonymity set            | Millions of users blending together      | Just you — no crowd                     |
| Who runs the nodes       | Volunteers worldwide                     | You control all nodes                   |
| VPN integration          | Optional via bridges                     | ✅ Built in by design                   |
| Dashboard / visibility   | ❌ Black box by design                   | ✅ Glass box — core feature             |
| Educational transparency | ❌ Not the goal                          | ✅ The entire point                     |
| Production ready         | ✅ Yes — battle tested                   | ❌ Research and lab use only            |
| Resistant to correlation | ✅ Strong (large anonymity set)          | ❌ Weak (you own all nodes)             |
| Purpose                  | Real anonymity on the internet           | Learning, research, home lab            |

## The Most Important Difference:

Tor's real power does not come from encryption alone. It comes from
**how many people use it simultaneously**. When millions of users
route traffic through the same nodes, an observer cannot tell which
stream belongs to which user. This is called the **anonymity set**.

PrivacyNet Lab has no anonymity set. You control all the nodes, so
an observer who knows it is your lab already knows the traffic is yours.
This is intentional — the goal here is learning, not hiding.

```
Tor:
  User A ─┐
  User B ─┼──► [Guard] ──► [Middle] ──► [Exit] ──► Internet
  User C ─┘
  Observer cannot tell which user generated which traffic.

PrivacyNet Lab:
  You ──────────► [Node 1] ──► [Node 2] ──► [Node 3]
  Observer knows it is your lab. That is fine — it is a learning tool.
```

---

## What PrivacyNet Lab Adds That Tor Does Not Have

### 1. The Glass Box Model
Tor is deliberately opaque. PrivacyNet Lab does the opposite — it
shows you in real time exactly what each node can and cannot see.
This makes abstract cryptography concepts tangible.

### 2. Built-in VPN Layer
The Host + VM architecture wraps all traffic in a VPN tunnel before
it enters the routing chain. This adds a transport encryption layer
that Tor does not include by default.

### 3. Educational Dashboard
A live Flask dashboard shows per-node views side by side. You can
watch encryption layers being stripped in real time. Tor has no
equivalent because transparency is not its goal.

### 4. Fully Local and Sandboxed
PrivacyNet Lab runs entirely on your own machines. No external nodes,
no public internet dependency, no risk of affecting others. This makes
it safe to experiment, break things, and learn.

---

## What PrivacyNet Lab Intentionally Does Not Do

- ❌ Provide real anonymity on the public internet
- ❌ Replace or compete with Tor in any way
- ❌ Route traffic through untrusted third-party nodes
- ❌ Evade law enforcement or legal oversight

---

## Intellectual Honesty

PrivacyNet Lab would not exist without the foundational research
behind Tor and onion routing, originally published by the U.S. Naval
Research Laboratory in the 1990s. This project is a learning tribute
to those concepts, not a replacement or competitor.

If you need real anonymity, use Tor.
If you want to understand how it works from the inside — use PrivacyNet Lab.

---

*PrivacyNet Lab — Educational use only.*
