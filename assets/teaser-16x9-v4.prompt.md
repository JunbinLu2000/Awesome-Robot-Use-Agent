# Robot Use Agent teaser — bottom cards removed

- Tool: built-in imagegen.
- Source: the user's first image, with the second image as the white edit-region mask.
- Change: remove all three bottom information cards and restore the pale paper background.
- Preserved: progression arrow, three stage captions, main scene, headline and subtitle.
- Final: `teaser-16x9-v4.png`, 1680 × 945 pixels, exact 16:9 with narrow white export padding.
- Visual check: all three cards removed; the long arrow and main scene remain intact.

## Prompt

Edit image 1 using image 2 as a selection mask: WHITE is the area to erase, BLACK is the area to preserve. Image 1 is the exact artwork to edit; image 2 is not artwork.

Remove the entire bottom row of THREE rounded rectangular information cards, including all borders, colored backgrounds, icons and text:
- left purple "General-Purpose AI" / "Reason and plan" card and brain icon;
- middle peach "Robot Interfaces" / "Sensor and actuator APIs" card and arm icon;
- right green "Physical Embodiments" / "Arms, mobile robots, and more" card and wheeled robot icon.
These are the only elements being deleted. Replace the whole selected bottom strip with the clean near-white lightly textured paper background already surrounding the cards. Leave no ghost outlines, fragments, text, icons, colored fills or replacement content.

Preserve the long horizontal lavender-to-mint arrow immediately ABOVE the cards, including its complete outline, arrowhead, and the exact text "From digital tools to physical interaction". Also preserve all three stage captions "Computer Use", "Robot Use", "Physical World", the entire house and outdoor scene, every robot and person, AI Agent cloud and Robot APIs, all upper arrows, headline and subtitle. Keep every unselected element at its original size and position as closely as possible. Do not redesign, crop, reflow, enlarge the main scene, restore the previously removed footer, or add anything. Preserve the landscape 16:9 composition and the original pencil/pastel style. Output the complete edited image with an empty near-white bottom area where the cards were.
