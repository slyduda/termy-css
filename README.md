# TERMY lite

Termy lite is an experimental version [Termy](https://termy.gg). Built versions on this project are comprised only of HTML and CSS for consumption on [cohost.org](https://cohost.org).

# How it works

There are a few ways we can "create state" from HTML and CSS. One method relies on us using checkboxes and the :checked pseudo selector to match various states with what we want our application to accomplish. Using multiple keyboards for every letter we can create various permutations of guesses based on our target puzzle by using the termy solve algorithm located in /util/termy.py. This method gives us a linear way of building Termy without any JavaScript, but unfortunately for our use case, it does not work. Cohost does not allow pseudo selectors because it does not allow external CSS style sheets. As a result, we have to use the only other method to recognize "state" in HTML - the detail > summary, contents method. This method is tricky because it relies on creating a new keyboard for *every key* in the previous keyboard, making this method exponential. Pair this up with specific sizings for keys and keyboards along with result styling and more, this file gets large quick.

At first, the intent was to create a 4x4 game of Termy with a limit of 10mb due to the upgraded upload limit for paying members that cohost has. Upon further inspection, this metric is not for html but for media uploads with 500kb being the undetermined file size cap. The current size of a 3x1 game (3 letter and 1 guess) Termy Inline is about ~700mb without all of the classes transposed into their respective styles. If we are able to shrink this file down we will be able to post 4 or 5 individual 3x1 Termy games sequentially in a Cohost post to allow users to play Termy like normal (kinda...).

Work on this will be haulted until further testing is done on Cohost post limits.

# Commands

### Build Inline Style Version

```
build.py
```

### Build Pseudo-Selector Version

```
app.py
```