# Robot Use Agent teaser — footer removal

- Tool: built-in imagegen.
- Edit target: the exact first image supplied by the user, `exec-f8c246bb-66eb-4bd2-bb9b-dc36cd3982cb.png`.
- Selection: white area in the user-supplied second image.
- Change: remove the footer text beneath the cards and restore the near-white background.
- Final: `teaser-16x9-v3.png`, 1680 × 945 pixels, with narrow white export padding to maintain exact 16:9.
- Visual check: footer removed; three cards and the main scene retained.

## Prompt

Use image 1 as the exact edit target and image 2 only as the black-and-white selection mask. The white painted area near the bottom center of image 2 identifies the content to remove. Black means preserve.

Remove the bottom footer text "Articles · Papers · Projects · Benchmarks" from image 1. Fill that small footer area with the same clean, near-white lightly textured paper background as its immediate surroundings. The mask slightly overlaps the very bottom of the middle card; preserve and seamlessly restore the middle card's bottom border, without altering any of the three cards. The intended removal is the footer text beneath the cards.

Preserve every other part of image 1 as closely as possible: full headline and subtitle, AI Agent, Robot APIs, observations/actions arrows, all three scene regions, people and robots, both doorways, three stage captions, the long progression arrow, the three bottom cards with all their icons and text. Do not redesign, shift, resize, crop, or change any other wording or objects. Do not add any replacement text. Keep the landscape 16:9 composition and the existing pencil/pastel watercolor style. Return the complete edited artwork, never the mask.
