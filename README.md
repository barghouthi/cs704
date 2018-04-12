# CS 704: Principles of Programming Languages (Spring 2018)

| τ | τ' |
|-|-|
|When | Tu/Th 230-345 |
|Where | CS 1325 |
|Who | [Aws Albarghouthi](http://www.cs.wisc.edu/~aws) |
|Office hours | Tue 100-200 in CS 6363 |

All notes and assignments wil be posted on this website. 

Submission of assignments and course project deliverables is via [canvas](https://canvas.wisc.edu/courses/77585).

## Course description
This course covers a range of topics in programming languages, including lambda calculus and type theory, functional programming, logics for encoding programs, and automated verification techniques.

The goal is to expose students to a range of mathematical and practical tools for reasoning about programs.

## Lectures
The following will be populated as the course progresses:

#### Week 1 (Jan 22) Lambda calculus

* **Tue** Welcome to the course / Intro to the beautiful lambda calculus
  * [notes](notes/cs704-lec-1-22-2010.pdf)
  * Ch. 5 of TAPL 

* **Thu**  Computing with lambda calculus
  * [notes](notes/cs704-lec-01-25-2010.pdf) 
  * Chs. 5 and 6 of TAPL
  
*you might also find helpful the notes from Sampson's Cornell class—[this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec02.pdf) and [this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec03.pdf)*

#### Week 2 (Jan 29) Programming constructs & fixpoints in lambda calculus
* **Tue** Programming constructs in lambda calclus
  * [notes](notes/cs704-lec-01-29-2010.pdf)
  * Ch. 5 of TAPL 

* **Thu**  Fixpoints in lambda calculus
  * [notes](notes/cs704-lec-01-29-2010.pdf) (same as Tue)
  * [code from class](code/fixpoint_combinators.py)
  *   <a href="http://matt.might.net/articles/implementation-of-recursive-fixed-point-y-combinator-in-javascript-for-memoization/"> Matt Might's blog: Y combinator in JS</a>
        (See Might's other lambda calculus posts too.)

[*Asn 1 out*](http://pages.cs.wisc.edu/~aws/courses/cs704-asn/asn1)
<!--assignment 1 release-->

#### Week 3 (Feb 5) The Church–Rosser theorem / FP
* **Tue** Deep dive into functional programming
  * *no notes—tonnes of online tutorials*
 
* **Thu** The Church–Rosser theorem
  * [notes](http://pages.cs.wisc.edu/~horwitz/CS704-NOTES/1.LAMBDA-CALCULUS.html#churchRosser)

*Deliverable 1 due*

#### Week 4 (Feb 12) Types
* **Tue** Introduction to types
  * Ch. 8 of TAPL
  
* **Thu** Simply typed lambda calculus	
  * Ch. 9 of TAPL

*you might also find helpful the notes from Sampson's Cornell class—[this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec19.pdf) and [this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec20.pdf)*

*Asn 1 due* /
[*Asn 2 out*](asn/asn2.pdf)


<!--assignment 1 due-->
<!--assignment 2 release-->

#### Week 5 (Feb 19) Type inference & polymorphism
* **Tue** Type inference
  * Ch. 22 of TAPL
  
* **Thu** System F **cancelled due to baby**
  * Ch. 23 of TAPL
  
*you might also find helpful the notes from Sampson's Cornell class—[this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec23.pdf) and [this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec24.pdf)*

####  Week 6 (Feb 26) Semantics
* **Tue** Operational semantics
  * The class presentation is based on Nielsen and Nielsen's book [Sem] -- see their comprehensive slides [here](http://www.imm.dtu.dk/~hrni/SWA/SwA_presentations/SwA-2a-natural.pdf)
  
  
* **Thu** Axiomatic semantics
  * The class presentation is based on Nielsen and Nielsen's book [Sem] -- see their comprehensive slides [here](http://www.imm.dtu.dk/~hrni/SWA/SwA_presentations/SwA-9-axiomatic.pdf)

*you might also find helpful Chs 7 (operational semantics) and 12 (axiomatic semantics) of [Chlipala's FRAP book](http://adam.chlipala.net/frap/"), which is freely available*


<!--assignment 2 due-->
<!--assignment 3 release-->

####  Week 7 (Mar 5) Logic & SAT/SMT
* **Tue** Propositional logic and SAT solvers
  * The class presentation will follow Dillig's slides: [here](http://www.cs.utexas.edu/~isil/cs389L/lecture1-6up.pdf) and [here](http://www.cs.utexas.edu/~isil/cs389L/lecture2-6up.pdf)
  
  
* **Thu** First-order logic and SMT solvers
  * The class presentation will follow Dillig's slides: [here](http://www.cs.utexas.edu/~isil/cs389L/lecture6-6up.pdf) and [here](http://www.cs.utexas.edu/~isil/cs389L/lecture7-6up.pdf) and [here](http://www.cs.utexas.edu/~isil/cs389L/lecture10-6up.pdf)

*For more references, consult Bradley and Manna's book [CofC]—see references below*

*Asn 2 due* /
*Deliverable 2 due* /
*[Asn 3 out](asn/asn3.pdf)*

####  Week 8 (Mar 12) Transition systems & program encodings

* **Tue** Bounded encodings
  * [notes](notes/transRelEnc.pdf)
 
* **Thu** Bounded encodings and Z3 tutorial
  * same notes as Tue
  * [code from lecture](code/z3/z3tut.py)



#### Week 9 (Mar 19) Automated verification
* **Tue** Finding Hoare proofs with Horn clauses
  * [notes](notes/hornClauses.pdf)
 
* **Thu** Automatically solving Horn clauses / intro to assignment 4
  * same notes as Tue
  * we will also cover k-induction, the subject of asn3, which is covered in Sec 8 of the [notes from last week](notes/transRelEnc.pdf)
  
*Asn 3 due* /
*[Asn 4 out](asn/asn4.pdf)*
<!--assignment 3 due-->
<!--assignment 4 release-->

#### Week 10 (Mar 26) SPRING BREAK


####   Week 11 (Apr 2) Automated verification continued
* **Tue** Implementing a mini verifier
  * [code](code/z3/miniverif.py)
 
* **Thu** Dealing with recursion
  * to be added

<!--assignment 4 due-->
<!--assignment 5 release-->

#### 🔥 Week 12 (Apr 9) Handling concurrency
* **Tue** To understand concurrency proof rules, we begin with recurisve proofs
  * [code](code/z3/mccarthy91.py)
  * [notes](notes/hornClauses.pdf) see section on recursion (more details to be added)
 
* **Thu** Rely-Guarantee Proofs
  * notes to be added
  
 *Deliverable 3 due*

#### Week 13 (Apr 16) Abstract Interpretation

*Asn 4 due* / 
*Asn 5 released* 

#### Week 14 (Apr 23)
* Class presentations will be held this week.
#### Week 15 (Apr 30)
* Class presentations will be held this week.

*Asn 5 due* /
*Deliverable 5 is due May 11*
## Assignments
Assignments will be posted here:

| Assignment | Due date |
| - | - |
| [asn1](http://pages.cs.wisc.edu/~aws/courses/cs704-asn/asn1)  | Feb 15 |
| [asn2](asn/asn2.pdf)  | ~~Mar 1~~ Mar 8 |
| [asn3](asn/asn3.pdf)  | Mar 22 |
| [asn4](asn/asn4.pdf)  | Apr 17 |

## Evaluation
Performance will be evaluated as follows:

| Task | X% |
| - | - |
| Research project | 45% |
| Assignments (5) | 40%|
| Project presentation | 10% |
| Class participation | 5% |


## Course Project
For the final project, you can work on a problem of your choice with a partner or by yourself.

* **Deliverable 1 (Feb 5)**   Send me a list of three project ideas.

* 5%: **Deliverable 2 (Feb 26)**  Submit a 2-3 page proposal including the following:
The statement of the problem to be investigated
An explanation of why the problem is interesting
A description of what you propose to do.
Explain the elements that you will have to build.
Explain the elements that you can pick up from open-source sites.
Explain the experiment(s) or performance measurement(s) that you plan to carry out. Two good approaches are
State the hypothesis that you hope to refute.
Complete the following sentence: "The experiments were designed to shed light on the following questions: . . ."
Then explain what you plan to measure; how you will measure it (if it is not obvious); and where you will obtain test cases.
List the tasks, broken down into two or three milestones

* 5%: **Deliverable 3 (Apr 12)** Submit a description of progress, implementation plan with completed steps checked off, and experimentation plan. Please turn in an updated proposal (with changes marked with changebars, and your new material added as "Appendix B: Progress Report".

* 10%: **Deliverable 4 (last 2 weeks of class)** 10-minute oral presentations (plus 5 minutes for questions/discussion) will be given during class. You will need to e-mail me an abstract (in plaintext) giving the title, project participants, and a two-paragraph to three-paragraph summary of what will be presented.

* 35%: **Deliverable 5 (May 11)** Final writeup: The final writeup should be modeled after a typical conference paper. There is no length requirement or limit, but I would expect it to be somewhere around 6-10 pages of ACM's double-column conference formats. 

## Resources
There are no required textbooks for this class. The following is a list of books that should be  useful references for different parts of the course.

This is an excellent reference for our lambda calculus and types material

* [TAPL] Pierce, <a href="https://search.library.wisc.edu/catalog/999923278402121"> Types and Programming Languages.</a> The MIT Press, 2002.

This is a free and excellent book that covers most material we cover in 704

* [FRAP] Chlipala <a href="http://adam.chlipala.net/frap/">Formal Reasoning About Programs</a>


This book talks about decision procedures
and their applications in verification.

* [CofC] Bradley and Manna, <a href="http://search.library.wisc.edu/catalog/ocn190764844"> The Calculus of Computation.</a> Spring, 2007.

This is a short book on
operational, axiomatic, and denotational semantics.

* [Sem] Nielson and Nielson <a href="http://www.imm.dtu.dk/~hrni/SWA/swa.html"> Semantics with Applications.</a> Springer, 2007.

The following book covers data-flow analysis
and abstract interpretation.

* [PA] Nielson et al., <a href="http://search.library.wisc.edu/catalog/ocm42579405"> Principles of Program Analysis </a> Springer, 1999.

This is another abstract interpretation resource.

* [AI] Abramsky and Hankin, <a href="https://www.cs.virginia.edu/~weimer/2007-615/reading/AbramskiAI.pdf"> An Introduction to Abstract Interpretation.</a>
  
There are multiple courses at other universities
that overlap with the material we cover in CS704. Here are some that I found helpful:

* <a href="https://www.cs.cmu.edu/~15414/schedule.html"> Fredrikson & Platzer's course at CMU </a>
* <a href="https://www.cs.cornell.edu/courses/cs6110/2018sp/schedule.html"> Sampson's class at Cornell </a>
