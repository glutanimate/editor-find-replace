Provides a **find and replace dialog** in the **Editor** that alternatively allows for free-form **text replacements** or **updating cloze indexes** in selected text.

**SCREENSHOT**

![](https://raw.githubusercontent.com/glutanimate/editor-find-replace/master/screenshots/find_and_replace.png)

**COMPATIBILITY**

This add-on only works with Anki's stable release branch (2.0.x ≥ 2.0.30). The 2.1 beta branch is **not supported** at this point in time.

**USAGE**

The find and replace dialog can either be invoked by clicking on the provided button or using the assigned shortcut (`Ctrl+T, R`, i.e. press Ctrl+T, release the keys, press R).

You can either choose to replace specific phrases, or to update instances of a specific cloze index to a new number.

Replacements will be performed on the current text selection. If you don't select anything before invoking the dialog, the add-on will automatically act on the entirety of the current field.

Actions can be reversed by using Anki's default undo shortcut (`Ctrl+Z`)

**LIMITATIONS**

Like Anki's built-in find-and-replace dialog, this add-on works on the HTML-level. As a result, you might not be able to replace strings that you think you should be able to replace.

For instance, if a phrase is partially bo**ld** then the underlying HTML code would look like this: `bo<b>ld</b>`. In that case the add-on would only be able to find that sequence with the keyword `bo<b>ld</b>`, and not with `bold`.

**CHANGELOG**

2017-08-16 – Initial release

**SUPPORT**

Please **do not report issues or bugs in the review section below**, as I will not be able to reply to them nor help you. Instead, please report all issues you encounter either on [GitHub](https://github.com/glutanimate/editor-find-replace/issues), or by posting a new thread on the [Anki add-on support forums](https://anki.tenderapp.com/discussions/add-ons) while mentioning the name of the affected add-on in your thread title.

**CREDITS AND LICENSE**

*Copyright (c) 2017 [Glutanimate](https://github.com/Glutanimate)*

This add-on was commissioned by a fellow Anki user. All credit for the original idea goes to them.

Licensed under the [GNU AGPLv3](https://www.gnu.org/licenses/agpl.html). The code for this add-on is available on [![GitHub icon](https://glutanimate.com/logos/github.svg) GitHub](https://github.com/Glutanimate/editor-find-replace).

**MORE RESOURCES**

A lot of my add-ons were commissioned by other Anki users. If you enjoy my work and would like to hire my services to work on an add-on or new feature, please feel free to reach out to me at:  ![Email icon](https://glutanimate.com/logos/email.svg) <em>ankiglutanimate [αt] gmail . com</em>

Want to stay up-to-date with my latest add-on releases and updates? Feel free to follow me on Twitter: [![Twitter bird](https://glutanimate.com/logos/twitter.svg)@Glutanimate](https://twitter.com/glutanimate)

New to Anki? Make sure to check out my YouTube channel where I post weekly tutorials on Anki add-ons and related topics: [![YouTube playbutton](https://glutanimate.com/logos/youtube.svg) / Glutanimate](https://www.youtube.com/c/glutanimate)
