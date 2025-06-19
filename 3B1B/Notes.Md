### From Legend himself

So this tutorial is from the creator himself to show the engine and the workflow.

### There are 2 versions

1. Which he created himself
2. Opensource version Manim community version

### Hello World

Every scene is a class in Python, and functions will have the actual animation code.

One thing I got to know here is he, connected the shell with the actual scene, and renders just the part of it to check each time. It is the customization he done for himself. 

For now I don't know much so I saw one similar alternative

To skip the animations happened before I can use this throughout my code.
self.next_section("Section Name", skip_animation=True) 

## add() play()

add() - add the object 
play() - to play the animation on that object.

## Transform()
Anything can turn anything in Manim


### 3D

Manim is always in 3D, he is showing in the canvas by moving around his mouse.
I think it is something part of OpenGL which manim uses under the hood to animte.


## Opacity of background

Add the following before class

```python
config.background_color = WHITE
config.background_opacity = 0.5
```