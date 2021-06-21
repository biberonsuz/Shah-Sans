# Shah-Sans
Python generated variable font

# Future Expansion
- issues
	- dieresis x coordinates switching when width is smaller
	- round corners getting shorter than the thickness when r<0.1 (maybe minR should be 0.05?)
	- glyph_k is very weird looking
	- cedilla height distorts on t<25
	- cedilla width distorts on w<400
	- spacing with width>500
	- contrast = 0 after CNTR>.85(?)
	- glyph_w too thick, glyph_k diagonals too thicks
- make ascender and descender variable axes (tried doing these, uses more than 60% of my RAM)
- solve RAM overloading after executing script (how to 'empty' ram after the master objects have been used)
- kerning ???
- ligatures ???
- make italic axis with serifs

