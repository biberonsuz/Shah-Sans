# Shah-Sans
Python generated variable font

# Future Expansion
- issues
	- dieresis x coordinates switching when width is smaller
	- round corners getting shorter than the thickness when r<0.1 (maybe minR should be 0.05?)
	- glyph_t
	- g missing rounded serif on top
	- glyph_k is very weird looking
	- cedilla height distorts on t<25
	- cedilla width distorts on w<400
	- glyph_r disappears when width<200
	- spacing with width>500
	- contrast = 0 after CNTR>.85(?)
- make ascender and descender variable axes (tried doing these, uses more than 60% of my RAM)
- make rounded serifs components? (like in glyphs) this way they could be adjusted with the r value
- solve RAM overloading after executing script (how to 'empty' ram after the master objects have been used)
- kerning ???
- ligatures ???
- dots could get boxier on less roundness
- make italic axis with 
