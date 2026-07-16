# Architecture Document Skeleton

Copy the block below into the target project's `ARCHITECTURE.md`, then
rework it: keep only the sections this project actually offloads from its
entrypoint (no empty stubs), replace placeholders with real content, and
write human-readable prose — this is a public-convention file, not an
agent-terse one. Each `##` heading is a pointer target: entrypoint pointers
reproduce it byte-exactly, so renaming a heading means updating every
pointer to it in the same change.

````markdown
# Architecture

<One paragraph: what this system is, for a reader seeing it first. Note
that the agent entrypoint points into the sections below.>

## Overview

<How the main parts fit together; a diagram or a short prose walk-through.>

## Tech Stack

<Languages, frameworks, notable dependencies, and why they were chosen
where the reason still matters.>

## Layout

<The directory map: one line per top-level area, what lives there.>

## Key Flows

<The two or three flows someone must understand before changing anything:
request path, data pipeline, build/release — whichever apply.>

## Decisions

<Recorded design decisions that still bind: the decision, the reason, and
what would trigger revisiting it.>
````
