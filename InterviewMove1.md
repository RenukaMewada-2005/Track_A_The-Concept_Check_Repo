# MOVE 1: BE THE EVAL YOURSELF

**Concept Tested:** Frontend vs Backend

---

## Interviewee 1: Shruti

### Question 1:
What is a frontend, what is a backend, and why do we need both?

### Answer:
"So frontend is like the part of an application or website that we(users) can see and interact with. Things like buttons, text boxes, images,.. that appear to the user.

And backend is where the work happens behind the scenes. Basically, it might process the requests, store data and communicate with databases.

We need both because users only need an interface to interact (which is frontend), while the actual processing and data handling happen separately in the background (which is backend)."

### Follow-up Question:
If a modern frontend browser can execute complex JavaScript logic perfectly fine, why can't we just run all our database queries and secret business logic directly inside the user's browser? Why do we waste money running a separate backend server at all?

### Answer:
"To be honest, I'm not sure about this.

If everything was in the frontend, users would be able to see the code. I feel there needs to be a layer that handles sensitive information, stores data, and controls what users can and cannot do.

So my guess is that the backend exists mainly for security or control. Also, data management maybe.

But beyond that, I'm not confident enough to explain it from first principles."

### Evaluation:
Shruti demonstrated a good definition-level understanding of frontend and backend. However, when challenged with a first-principles architectural question, she was unable to clearly explain why a backend is fundamentally necessary. She identified security and control as possible reasons but lacked confidence in deriving the explanation from underlying system constraints.

### Gap Identified:
Can describe what frontend and backend do, but cannot explain why a backend must exist when browsers are already capable of running complex JavaScript.

---

## Interviewee 2: Sagar

### Question 1:
What is a frontend, what is a backend, and why do we need both?

### Answer:
"Frontend: as the name suggests - It's in the front, which means it's on the side of the user / consumer / customer whoever is interacting with our system. Whatever happens in connection with the user directly is frontend.

Backend: All those things that the user cannot see are parts of backend. A query being asked on UI goes to the server, then to the database, fetches the information and sends a response back.

Each system is connected to other systems through APIs, which are connectors and sets of rules that both systems understand."

### Follow-up Question:
If a modern frontend browser can execute complex JavaScript logic perfectly fine, why can't we just run all our database queries and secret business logic directly inside the user's browser? Why do we waste money running a separate backend server at all?

### Answer:
"We spend money on running separate backend servers because:

* The data stored is in control with us and sits on our systems.
* Because it's not rendered on the user's browser, their access is quite limited which can also be controlled.
* Each API comes with a logic and a unique key, which helps in protecting the data and only allowing required connections."

### Evaluation:
Sagar demonstrated a stronger operational understanding than Shruti and identified several practical reasons for using a backend, including control of data, limited user access, and API protection. However, his explanation remained largely based on common industry practices and security considerations. He did not fully derive the architectural necessity of a backend from first principles such as trust boundaries, shared state management, authority, and ownership of business logic.

### Gap Identified:
Can explain several practical reasons for having a backend, but cannot fully derive the fundamental architectural reasons why sensitive logic, shared data, and system authority cannot be entrusted entirely to the client browser.

---

## Common Pattern Observed

Both interviewees were able to define frontend and backend and describe their roles at a surface level.

However, when challenged with the question:

"If browsers can already execute complex JavaScript, why do we need a backend at all?"

both struggled to provide a first-principles explanation.

### Observed Gap:
Learners can often describe what frontend and backend do, but struggle to explain why a backend must exist from an architectural perspective.
