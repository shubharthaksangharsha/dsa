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

✍️ Essay 1: Is COMPAS biased? Is it unfairly biased?

Introduction

The COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) algorithm is used in U.S. courts to predict the likelihood of reoffending. This case raises concerns about algorithmic bias and fairness. To decide whether COMPAS is unfairly biased, we must distinguish between statistical bias and social unfairness, and question whether understanding its process is essential for ethical judgment.

Main Discussion

ProPublica’s 2016 investigation revealed that COMPAS systematically overestimated recidivism risk for Black defendants and underestimated it for White defendants. This shows unequal false positive and false negative rates. From a fairness perspective, this means outcomes differ by race even when criminal records are similar.

Northpointe, the company behind COMPAS, argued that their system is “calibrated” — meaning that among people given the same risk score, the probability of reoffending is roughly equal across groups. However, calibration and equal error rates cannot both be satisfied when base rates differ. This highlights a conflict between mathematical fairness criteria and social justice fairness.

Whether understanding the algorithm’s internal process is necessary depends on what we value. If fairness is about outcomes, then we can judge bias statistically. But if fairness involves intent or mechanism, we must understand the internal workings — such as which variables (e.g., race proxies) influence predictions.

Conclusion

COMPAS is statistically biased and socially unfair because its predictions reinforce existing racial disparities. Even without full transparency, unequal outcomes across groups show unfair bias. Understanding the process deepens the ethical critique but is not required to see the harm.


---

✍️ Essay 2: What is being “aligned” in the alignment problem?

Introduction

The “alignment problem” in AI ethics asks whether artificial intelligence systems act according to human values. To understand what is “being aligned,” we must identify what AI is aligned with — human goals, moral norms, or social outcomes.

Main Discussion

Alignment concerns how AI’s objective functions or reward signals reflect human intentions. In practice, AI agents are optimized to maximize numerical rewards or accuracy. But human values — such as fairness, compassion, or justice — are complex, context-dependent, and often conflicting.

Philosophically, alignment means ensuring that the behavior of an AI corresponds to the intentions of its designers or users. Misalignment occurs when systems achieve objectives in unintended or harmful ways (e.g., a recommendation algorithm maximizing engagement but promoting misinformation).

Moral alignment extends beyond technical optimization. It involves normative reasoning: AI should respect ethical principles that humans endorse collectively. Hence, alignment is not only about the relation between “AI goals” and “human commands,” but also about embedding moral reasoning and accountability into design.

Conclusion

What is being “aligned” is the relationship between machine goals and human values. Achieving alignment means creating systems that not only follow instructions but also promote ethically acceptable and socially beneficial outcomes.


---

✍️ Essay 3: Is there an algorithmic solution to the alignment problem? (Klein & Kasirzadeh)

Introduction

Klein and Kasirzadeh argue that alignment cannot be fully solved through algorithms alone. The question is whether ethical alignment — ensuring AI acts according to human values — can be achieved by computation, or whether it requires continuous human involvement.

Main Discussion

They introduce the idea of asymmetric necessitation — the relationship between facts about algorithms and moral facts. In simple terms, even if an algorithm perfectly tracks human preferences, moral correctness does not necessarily follow. The connection is one-way: moral truths might determine what an aligned system should do, but not the reverse.

This implies that no purely technical method — no optimization, loss function, or reward shaping — can guarantee moral correctness. Moral reasoning involves context, interpretation, and judgment that extend beyond data patterns.

Algorithmic tools can approximate human preferences, but human oversight, deliberation, and institutional ethics remain essential. Thus, alignment is partly social and political, not just computational.

Conclusion

There is no purely algorithmic solution to the alignment problem. As Klein and Kasirzadeh show, alignment depends on human moral reasoning. Algorithms can assist but cannot replace ethical deliberation.


---

✍️ Essay 4: Can there be such a thing as “algorithm washing”?

Introduction

“Algorithm washing” refers to the practice of using algorithms to appear objective or fair while actually hiding bias, responsibility, or unethical practices. It parallels “greenwashing” — when companies exaggerate environmental responsibility to look good publicly.

Main Discussion

Organizations may claim that algorithmic systems make “neutral” decisions, thus distancing themselves from accountability. For example, a company may use automated hiring tools and blame discrimination on the “algorithm,” rather than on biased data or design choices.

This is problematic because algorithms reflect the values and assumptions of their creators. By presenting them as impartial, institutions avoid scrutiny and ethical responsibility. Algorithm washing thus obscures moral agency and undermines trust.

The phenomenon highlights the importance of transparency, explainability, and human oversight. Ethical AI governance requires acknowledging that every model involves normative choices — in data selection, labeling, and evaluation metrics.

Conclusion

Yes, algorithm washing exists. It happens when organizations use algorithms to shift or hide responsibility under a façade of objectivity. Recognizing this helps promote accountability and genuine fairness in AI systems.


---


✍️ Essay 5: Are techniques such as LIME or SHAPLEY adequate to detect and diagnose unfairness or discrimination?

Introduction

Techniques like LIME (Local Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations) are widely used to explain machine learning models. They aim to make AI systems more interpretable by showing how input features contribute to a model’s output. However, the question is whether interpretability tools alone can truly detect or diagnose unfairness and discrimination.

Main Discussion

LIME and SHAP provide local explanations, showing how features influence a single prediction. While this helps users understand individual decisions, it doesn’t reveal broader systemic biases. Fairness issues often occur at the dataset or group level — for instance, when a model performs differently across gender or racial groups.

LIME and SHAP assume that the model’s internal logic is reasonable and that fairness can be inferred from feature importance. But explainability is not the same as fairness: a transparent bias is still a bias. These tools show “how” a model decided, not “whether it should have decided that way.” Detecting discrimination requires fairness metrics (like demographic parity, equal opportunity) and social context beyond mathematics.

Moreover, these tools rely on approximations that can be unstable: small changes in data or random seeds may change the explanation. Therefore, depending solely on them may lead to false confidence in fairness.

Conclusion

LIME and SHAP are helpful but insufficient. They promote interpretability, not fairness. Detecting discrimination requires combining explainability with fairness auditing, bias testing, and ethical judgment by humans.


---

✍️ Essay 6: Can an AI make genuinely moral decisions if humans are not in the decision-making loop? If so, who is responsible for the consequences?

Introduction

Moral decision-making involves reasoning about right and wrong, considering intent, outcome, and responsibility. The question is whether AI — operating without human oversight — can make truly moral decisions, and if so, who bears responsibility for those actions.

Main Discussion

Current AI systems act through pattern recognition and optimization, not moral reasoning. They lack intentionality, consciousness, and empathy. Even when trained on moral datasets or human feedback, they only simulate moral reasoning, not understand it.

For example, a self-driving car choosing between two harmful outcomes may make a utilitarian choice based on programmed logic, not ethical deliberation. The decision may appear moral but is actually a reflection of human-coded priorities or data biases. Thus, moral responsibility cannot rest with the machine.

Responsibility lies with human agents — developers, designers, policymakers — who create and deploy AI. The “human in the loop” provides ethical oversight and context that algorithms cannot replicate. Without this, decisions risk being ethically blind even if technically accurate.

Some argue for machine moral agency — the idea that advanced AIs could one day possess autonomy deserving moral responsibility. However, as long as they lack genuine understanding and accountability, moral responsibility remains human.

Conclusion

AI cannot make genuinely moral decisions without human involvement. While it can execute ethically-informed rules, it lacks true moral understanding. Therefore, humans remain responsible for the outcomes of AI systems, both legally and ethically.


---



