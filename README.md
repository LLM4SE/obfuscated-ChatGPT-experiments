# Replication Package *Breaking the Silence: the Threats of Using LLMs in Software Engineering*

This repository encompasses the replication package associated with the research paper titled "Breaking the Silence: Unveiling Threats in the Application of Large Language Models (LLMs) in Software Engineering." The primary objective of this paper is to conduct a concise study elucidating certain limitations inherent in LLM-based research, along with offering guidelines (https://github.com/LLM4SE/guidelines) and example for their mitigation.

## Study Methodology

To execute our study, we leverage the capabilities of the software available at https://github.com/LLM4SE/obfuscated-ChatGPT. This specialized tool facilitates ChatGPT queries while additionally obfuscating the code within the queries. Our focus is on generating test cases for two specific Defects4J bugs: Chat-11 and Math-5. This process is iterated ten times to systematically observe the reproducibility of our approach.

## Results

The unprocessed outcomes of this experimental endeavor are conveniently housed in the `experiment-data/` directory.

The file `experiment-data/test-results.csv` contains the test execution results of the test genererated by ChatGPT.

Each file within `experiment-data/queries/<project>-<bug-id>/info-<timestamp>.json` encapsulates the details of an individual iteration. For every iteration, comprehensive results are documented, including the date, prompt, Defects4J information, and ChatGPT responses. Both unobfuscated and obfuscated code scenarios are considered for a thorough evaluation of the model's performance.

Result structrure: 
```js
{
  "date": "...",
  "bug": {
    "bugId": ...,
    "changedFiles": [
      "..."
    ],
    "diff": "...",
  },
  "original_prompt": "...",
  "obfuscated_prompt": "...",
  "original_res": {
    "response": "..."
  },
  "obfuscated_res": {
    "response": "...",
    "codes": "..."
  }
}
```