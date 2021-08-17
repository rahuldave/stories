+++
title = "Keeping Visualizations Simple with Matplotlib"
description = "Using matplotlib to remove Chartjunk from a plot"
date = 2021-08-17


[taxonomies]
topics = ["Visualization"]
+++


1.  In the thread <https://twitter.com/rahuldave/status/1425200284301725708>, I talked about the visualization in this image (from the financial times <https://www.ft.com/content/0f11b219-0f1b-420e-8188-6651d1e749ff?hcb=1>). How might we produce such visualizations.

![](/improvingfigures/1.png)




2. We'll tackle that question in another thread, but first we must learn how to make good plots using matplotlib. Which begs the question: what is a good visualization, and how can we make it?




3. Here are some of the best practices for visualization. We'll talk about the second one today: **Keep it simple!**. As Antoine de Saint-Exupéry said: *Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.*

![](/improvingfigures/3.png)




4. As @EdwardTufte who coined has persuasively argued in his books, extraneous visual elements that distract from the message should be removed. For example: tick-marks,frames, sometimes even numbers! Lets us carry this process using matplotlib for a simple example..

![](/improvingfigures/4.png)




5. Here is a dataset on electoral votes and population in all the US states. We'll make a bar chart comparing the electoral votes of different states. You can find the data and the analysis notebook for this thread HERE.

![](/improvingfigures/5.png)




6. This first snippet illustrates Matplotlib's object-oriented API. We first create a figure object, and in the context of that object, an axes object. Then pandas is used to place a bar plot into those axes. What's not so good about this image?

![](/improvingfigures/6.png)




7. In this picture taken from <https://end-to-end-machine-learning.teachable.com/p/navigating-matplotlib-tutorial-how-to/> by @_brohrer_, we see that (possibly multiple) Axes sit inside a Figure, and everything else (such as xaxis, yaxis, lines, patches, text, annotations) sits inside the Axes.

![](/improvingfigures/7.png)




8. How can we improve the previous image? Do we really need y-axis ticks with state names labeling them? How about we remove these ticks? We do this in matplotlib by setting their length to 0.

![](/improvingfigures/8.png)




9. Do we really need ticks on the x-axis? Why not just put the labels? And move these to the top because the longest bars are there. And then replacing the tick marks with a grid helps us see the values on each and every bar!

![](/improvingfigures/9.png)




10. Do the spines add anything to our presentation? No. The elements of the figure are strong enough to stand by themselves. Ok, so lets remove the spines...

![](/improvingfigures/10.png)




11. If you want to show more precise distinctions between the states' electoral votes, you want the grid (or tick marks if you were using those) to be more fine grained. So lets have a tick every 5 votes, which translates in our grid visual to a grid line every 5 votes.

![](/improvingfigures/11.png)




12. The tick-mark/grid-line labels look entirely redundant. After all, we can count off the grid-lines. So lets get rid of them, eliminate the clutter. And then, why not show the user the electoral votes for each state? Dont make the user think!

![](/improvingfigures/12.png)




13. The annotation is done by putting down text at an x of 1 greater than the electoral votes and a y obtained as a index (increasing from top to bottom) from the way matplotlib handles bar plots. We then let matplotlib clean up the layouting of the plot to make it look crisper.

![](/improvingfigures/13.png)




14. Maybe you want to see this image in your slides or website based on the color scheme you like, rather than having a white background. Then you can `savefig` the figure as a transparent png. There are multiple other save options as well.

![](/improvingfigures/14.png)




15. An incredible source to learn the ins and outs of @matplotlib is <https://end-to-end-machine-learning.teachable.com/p/navigating-matplotlib-tutorial-how-to/> by @_brohrer_ . I teach this stuff as well, as part of the Data Science courses at Univ.Ai.




16. This story is permalinked at <https://stories.univ.ai/improvingfigures/>. I'll soon be tweeting on re-producing the @FT vaccination plot I mentioned earlier. Follow me on twitter at @rahuldave and keep an eye on <https://stories.univ.ai> for more!

