🏸 Badminton Players Knowledge Graph
📌 Overview

This project demonstrates how to build and query a Knowledge Graph of badminton players using RDFLib and SPARQL in Python.

It stores information about players, their countries, and coaching relationships as RDF triples in the format:

Subject – Predicate – Object


For example:

P.V. Sindhu – playsFor – India  
P.V. Sindhu – coachedBy – Kim Ji-hyun


The project also allows users to enter a player’s name and retrieve relevant information interactively.

⚙️ Features

📂 Knowledge Graph Construction

Created RDF triples for badminton players, their countries, and coaches.

🔎 SPARQL Queries

Query player details (e.g., country, coach) from the graph.

⌨️ User Input

Users can enter a player’s name to extract info from the graph.

🧹 Regex Name Formatting

Applied regex to split and format player/coach names for consistency.
