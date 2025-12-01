# DSA - The Battle of Algorithms 

## Linked List Problems

| S.No | Problem Name                        | Solution Link                          |
|------|-------------------------------------|----------------------------------------|
| 1    | Custom Linked List Implementation   | [Solution](linkedlist/mylink.py)      |
| 2    | Find Middle of Linked List          | [Solution](linkedlist/middle_of_list.py) |
| 3    | Reverse a Linked List               | [Solution](linkedlist/reverse_linkedlist.py) |
| 4    | Reverse Linked List in K Groups     | [Solution](linkedlist/reverse_k_groups.py) |
| 5    | Check if Linked List is Circular    | [Solution](linkedlist/check_circular.py) |
| 6    | Detect and Remove Loop in Linked List| [Solution](linkedlist/detect_loop.py) |
| 7    | Remove Duplicates from Linked List  | [Solution](linkedlist/remove_duplicates.py) |
| 8    | Sort 0s, 1s, and 2s in Linked List  | [Solution](linkedlist/sort_0s_1s_2s_in_list.py) |
| 9    | Merge Linked Lists                  | [Solution](linkedlist/merge_ll.py) |
| 10   | Check if Linked List is Palindrome  | [Solution](linkedlist/check_pallindrome.py) |
| 11   | Add Two Linked Lists                | [Solution](linkedlist/add_two_list.py) |

## Array Problems

| S.No | Problem Name         | Solution Link                  |
|------|---------------------|-------------------------------|
| 1    | Find Largest        | [Solution](arrays/findlargest.py)     |
| 2    | Find Second Largest | [Solution](arrays/secondlargest.py)   |





--- 

# Do LLMs understand language in the same way as humans? Discuss the differences between LLMs in general and humans in general.

A recurring theme throughout this course is that surface-level behavioural similarity between humans and large language models (LLMs) should not be mistaken for shared cognitive architecture. Nowhere is this clearer than in the question of linguistic understanding. While contemporary LLMs such as GPT-4 generate syntactically sophisticated, context-appropriate sentences, the mechanisms by which they do so diverge fundamentally from the mechanisms described in human psycholinguistics. Drawing on the Chomsky/Systematicity lecture, the Language & Thought slides, and the Dual Process slides, I argue that LLMs do not understand language in the same way humans do, even if their outputs can be deceptively similar.

1. Systematicity and Productivity: Chomsky's Argument Against Associative Models

The Chomsky slides emphasised two core features of human linguistic competence: systematicity and productivity. Systematicity refers to the fact that if a human understands “3 + 4 = 7,” they automatically grasp that “4 + 3 = 7.” Likewise, if one understands the sentence “The dog chased the cat,” they also grasp “The cat was chased by the dog.” This structural generalisation is not learned by memorising string–string associations; it reflects mastery of rules or principles that govern allowable combinations.

Similarly, productivity reflects the capacity to generate indefinitely many new sentences from a finite set of rules. In class, we examined centre-embedding structures such as:

“The mouse that the cat that the dog painted taught sang.”

Humans struggle to process such sentences, but crucially they recognise them as syntactically well-formed because they possess an internalised system of hierarchical rules. This is exactly the point: human linguistic competence presupposes tree-structured, symbolic representations.

LLMs, by contrast, do not manipulate trees or rules. As the PPT put it: “LLMs do not manipulate symbols according to rules; syntax and semantics are not distinguished.” They are trained to predict the next most probable token given millions or billions of prior examples. When an LLM “understands” the Smarties task or generates a centre-embedded sentence, it is doing so through high-dimensional similarity structures, not through rule-based transformations. In the Chomsky slides, this is described as holistic similarity space, where relationships are encoded as distances rather than discrete features.

Therefore, while LLMs can approximate the outputs of rule-governed systems, there is nothing in their functional architecture that implements the combinatorial, algebraic properties underlying human language.

2. Linguistic Innateness and the Poverty of the Stimulus

Another point emphasised in lecture was the poverty of the stimulus argument: children reliably acquire complex syntactic principles despite receiving limited, noisy, and inadequate data. Because trial-and-error association cannot explain this, Chomsky concludes that the human mind must contain innate, domain-specific constraints that generate linguistic hypotheses.

LLMs, however, sidestep poverty of stimulus entirely by consuming datasets on a scale no human encounters. They succeed precisely because they do not learn like children: they rely on brute-force statistical coverage rather than inference under innate constraints. This difference is not merely methodological; it reflects a fundamentally different kind of cognitive process.

3. Strings vs Trees: What LLMs Encode

One of the most illuminating slides asked, “Strings or trees. Is Chomsky wrong?” Although LLMs operate exclusively on linear token sequences, linguistic structure in humans is hierarchical. Surprisingly, some tree-like dependencies emerge in LLM internal layers, but as the slides stressed, these are not explicitly represented. They are statistical artefacts detectable only through diagnostic probing, not components of the model’s functional computation.

This means LLMs simulate the outputs of a hierarchical grammar without actually employing one—a crucial difference. Humans infer structure; LLMs approximate it.

4. Dual-Process Cognition: Humans Use System 2, LLMs Don’t

The Dual Process PPT highlighted another deep architectural difference. Human language comprehension often requires System 2 reasoning: effortful, working-memory-dependent manipulation of hypotheticals, ambiguities, and syntactic embeddings. The frontal cortex supports “active maintenance,” enabling us to revisit assumptions, reinterpret ambiguous structures, and revise semantic commitments mid-sentence.

LLMs lack such mechanisms. Their processing is unidirectional and automatic, resembling a perpetual System 1 process. Chain-of-thought prompting only mimics System 2 reasoning—the model is still generating one token at a time with no genuine active maintenance. The slides emphasised that unlike humans, LLMs cannot decouple cognition from immediate input—there is no analogue of stimulus-independent prefrontal activity.

Thus, even when an LLM produces a multi-step explanation, it is not “thinking” in the way humans do; it is reproducing statistically correlated textual patterns.

5. Conclusion: Behavioural Similarity Without Cognitive Equivalence

Across all three relevant PPTs, the same conclusion emerges: LLMs do not understand language as humans do. Humans rely on innate rule-governed generative capacities, hierarchical syntactic structure, and dual-process cognitive architectures supporting active maintenance and metalinguistic reasoning. LLMs, by contrast, rely on similarity-based pattern extraction from massive corpora, lack linguistic modularity, and possess no mechanism analogous to human System 2 reasoning.

LLMs can perform understanding, but they do not possess understanding in the cognitive sense articulated in class.
--- 


