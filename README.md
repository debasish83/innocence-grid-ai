### Installation

python -m venv .venv

source .venv/bin/activate

pip install -e .

### Gemini API Key
Add your gemini API key in .env file

### PDF Parser

## summarize
pdf-parser summarize ./transcripts/Walker\,\ P74172\,\ 2025-01-29.pdf
## key points
pdf-parser keypoints ./transcripts/Walker\,\ P74172\,\ 2025-01-29.pdf

## ask
pdf-parser ask ./transcripts/Walker\,\ P74172\,\ 2025-01-29.pdf "Is there explicit signal: Direct statements of innocence for example I did not commit the crime, I am innocent, I did not do it"

No, there are no explicit statements of innocence from Calvin Walker.

On the contrary, he repeatedly takes responsibility for the murder of Daniel Chang and expresses deep remorse:

*   **Page 18, Lines 1-2:** When asked if he committed the murder in May 1998, he replies, "Yes."
*   **Page 22, Lines 19-21:** When asked if he shot Mr. Chang in a drug deal gone bad, he replies, "Yes."
*   **Page 30, Lines 12-17:** He states, "I shot Danny Chang 'cause I was a killer, a criminal minded, impulsive. And I felt, you know, I was scared. I felt challenged..."
*   **Page 31, Lines 20-24 & Page 32, Lines 1-4:** He admits to minimizing the shooting in a previous Risk Assessment, stating it wasn't true that the gun "just went off," and explicitly says, "No, that wasn't true at all. I, I was minimizing at that time, not understanding and taking full responsibility for my actions. But as I’m here and sit here today, I take full responsibility of my, of my actions..."
*   **Page 32, Lines 12-14:** He clearly states, "I had my hand around the trigger and I did pull the trigger and murder Daniel Chang. I take full responsibility for my actions."
*   **Page 88, Lines 23-25 & Page 89, Lines 1-9 (Closing Statement):** He begins by saying, "Please allow me to begin by expressing how deeply and sincerely sorry I'm for murdering Daniel Chang and for the immense suffering and pain that I caused his mother, Katie Chang, father, Eddie Chang, brothers, Roger, Roger and Steven Chang, and aunt as well, everyone else who loved and cared about Daniel as well. Daniel Chang was a good person who in no manner deserved what I did to Daniel." He later adds, "I'm certain if I was, if it wasn't for Daniel, if it wasn't for Daniel Chang, I would still be alive-- if it wasn't for me, Daniel Chang would still be alive today. I'm deeply sorry for all I caused in regards to all and everything that I've done."

## innocence-score
pdf-parser innocence-score ./transcripts/Walker\,\ P74172\,\ 2025-01-29.pdf

```json
[
  {
    "signal_type": "bias_language",
    "explanation": "The Presiding Commissioner refers to the inmate's past statements in a Risk Assessment where he "minimized the shooting, made it sound like an accident, like the gun just went off" (Page 31). Although the inmate now admits this was not true and takes full responsibility, the Board's focus on this past minimization (which the inmate describes as being 'in denial' and 'not being honest with myself' on Page 32) indicates how the system views and penalizes a lack of consistent, full accountability, even if not an outright claim of innocence."
  },
  {
    "signal_type": "bias_language",
    "explanation": "The Presiding Commissioner explicitly states, 'Choosing to lie, choosing to minimize. And unfortunately for you, you did minimize in the Risk Assessment' (Page 99). This institutional language highlights a negative judgment against the inmate's previous lack of complete honesty regarding the commitment offense. The Board uses this past minimization as evidence that his change and programming are 'neutral' at the time of the hearing (Page 101), indicating a bias against any historical attempt to lessen culpability."
  },
  {
    "signal_type": "bias_language",
    "explanation": "The Presiding Commissioner challenges the inmate's honesty regarding restitution avoidance, stating, 'I'm going to ask you again 'cause I don't think you were honest with me before' (Page 72) and later in the decision, 'as soon as you start losing credibility, it's difficult for us to weigh everything that you say because it bears on all the rest of your testimony' (Page 101). The Board's labeling of his responses as potentially dishonest or lacking credibility, and directly linking it to the assessment of his entire testimony and suitability, exemplifies institutional bias against perceived lack of transparency and full admission, even for behaviors outside the life crime itself."
  },
  {
    "signal_type": "bias_language",
    "explanation": "In the decision, the Commissioner states, 'I also think that your hope was maybe they don't know about it, maybe they can't find this out. And that's always problematic 'cause that's evidence of criminal thinking today' (Page 100). This statement interprets the inmate's 'forgetfulness' about recent restitution avoidance as a deliberate attempt to hide information, categorizing it as 'criminal thinking.' This demonstrates the institutional scrutiny and negative labeling of any perceived withholding of information or incomplete accountability, which is a key component in assessing suitability for parole."
  }
]
```

