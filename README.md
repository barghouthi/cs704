# CS 704: Principles of Programming Languages (Spring 2019)

| τ | τ' |
|-|-|
|When | Tu/Th 230-345 |
|Where | CS 1257 |
|Who | [Aws Albarghouthi](http://www.cs.wisc.edu/~aws) |
|Office hours | Tue 100-200 in CS 6363 |

All notes and assignments wil be posted on this website. 

Submission of assignments and course project deliverables is via [canvas](https://canvas.wisc.edu/courses/127564).

## Course description
This course covers a range of topics in programming languages, including lambda calculus and type theory, functional programming, logics for encoding programs, and automated verification techniques.

The goal is to expose students to a range of mathematical and practical tools for reasoning about programs.

## Lectures
The following will be populated as the course progresses:

#### Week 1 (Jan 21) Lambda calculus

* **Tue** Welcome to the course / Intro to the beautiful lambda calculus
  * [notes](notes/cs704-lec-1-22-2010.pdf)
  * Ch. 5 of TAPL 

* **Thu**  Computing with lambda calculus
  * [notes](notes/cs704-lec-01-25-2010.pdf) 
  * Chs. 5 and 6 of TAPL
  
*you might also find helpful the notes from Sampson's Cornell class—[this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec02.pdf) and [this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec03.pdf)*

#### Week 2 (Jan 29)
*Aws is at FAT* in Atlanta*

#### Week 3 (Feb 4) Programming constructs & fixpoints in lambda calculus

* **Tue** Programming constructs in lambda calclus
  * [notes](notes/cs704-lec-01-29-2010.pdf)
  * Ch. 5 of TAPL 

* **Thu**  Fixpoints in lambda calculus
  * [notes](notes/cs704-lec-01-29-2010.pdf) (same as Tue)
  * [code from class](code/fixpoint_combinators.py)
  *   <a href="http://matt.might.net/articles/implementation-of-recursive-fixed-point-y-combinator-in-javascript-for-memoization/"> Matt Might's blog: Y combinator in JS</a>
        (See Might's other lambda calculus posts too.)
        

#### Week 4 (Feb 11) Types
* **Tue** Introduction to types
  * Ch. 8 of TAPL
  
* **Thu** Simply typed lambda calculus	
  * Ch. 9 of TAPL

*you might also find helpful the notes from Sampson's Cornell class—[this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec19.pdf) and [this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec20.pdf)*

#### Week 5 (Feb 18) Type inference & polymorphism
* **Tue** Type inference
  * Ch. 22 of TAPL
  
* **Thu** System F 
  * Ch. 23 of TAPL
  
*you might also find helpful the notes from Sampson's Cornell class—[this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec23.pdf) and [this](http://www.cs.cornell.edu/courses/cs6110/2017sp/lectures/lec24.pdf)*

#### Week 6 (Feb 25) Semantics
* **Tue** Operational semantics
  * The class presentation is based on Nielsen and Nielsen's book [Sem] -- see their comprehensive slides [here](http://www.imm.dtu.dk/~hrni/SWA/SwA_presentations/SwA-2a-natural.pdf)
  
  
* **Thu** Axiomatic semantics
  * The class presentation is based on Nielsen and Nielsen's book [Sem] -- see their comprehensive slides [here](http://www.imm.dtu.dk/~hrni/SWA/SwA_presentations/SwA-9-axiomatic.pdf)

*you might also find helpful Chs 7 (operational semantics) and 12 (axiomatic semantics) of [Chlipala's FRAP book](http://adam.chlipala.net/frap/"), which is freely available*

#### Week 7 (March 4)
*Aws is at the Simons Institute in Berkeley*

#### Week 8 (March 11)

#### Week 9 (March 18)
*spring break*

#### Week 10 (March 25)

#### Week 11 (April 1)

#### Week 12 (April 8)

#### Week 13 (April 15)

#### Week 14 (April 22)
*project presentations*

#### Week 15 (April 29)
*project presentations*






## Assignments
Assignments will be posted here:

| Assignment | Due date |
| - | - |
| [asn1](http://pages.cs.wisc.edu/~aws/courses/cs704-asn/asn1)  | Feb 15 |


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

* 5%: **Deliverable 3 (Apr 10)** Submit a description of progress, implementation plan with completed steps checked off, and experimentation plan. Please turn in an updated proposal (with changes marked with changebars, and your new material added as "Appendix B: Progress Report".

* 10%: **Deliverable 4 (last 2 weeks of class)** 10-minute oral presentations (plus 5 minutes for questions/discussion) will be given during class. You will need to e-mail me an abstract (in plaintext) giving the title, project participants, and a two-paragraph to three-paragraph summary of what will be presented.

* 35%: **Deliverable 5 (May 10)** Final writeup: The final writeup should be modeled after a typical conference paper. There is no length requirement or limit, but I would expect it to be somewhere around 6-10 pages of ACM's double-column conference formats. 

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
