# Plate Loading Calculator Developer Report

Module 1 Critical Thinking

REFERENCE DRAFT — describes the reference implementation. Rewrite each answer
from your own rebuild experience before any submission.

## Purpose and intended use

The prototype computes which plates to load on each side of a barbell to
reach a target weight, a core feature planned for the WarrenFit fitness app.
When a target cannot be loaded exactly, it reports the closest loadable
weight below it rather than rejecting the input.

## Tools and libraries

The script uses Python 3 and only the standard library; plate weights are
exact binary fractions, so plain floats are sufficient. The loading math is
separated from the command-line interface so it can be tested independently
and reused behind the app's API later.

## Development challenges

The main challenge was discovering that the greedy heaviest-first strategy,
while always producing a valid loadout, does not always minimize plate count
(a 165 lb target yields three plates per side when two suffice). Deciding how
to handle unloadable targets, such as 137.7 lb, also required a design choice
between erroring and degrading gracefully.

## Future improvements

The next iteration should respect a limited plate inventory (pairs owned per
size), matching the equipment model in the full application, and add a
kilogram mode. A dynamic-programming pass could replace greedy selection to
guarantee the fewest plates.

## Lessons for broader development

Choosing the simplest data type the problem allows matters: this task is safe
with floats, while currency math is not. An algorithm that works is not
necessarily optimal, and stating a prototype's known limitations is part of
an honest handoff.
