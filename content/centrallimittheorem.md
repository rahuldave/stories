+++
title = "The CLT"
description = "Probably the 2nd most important theorem in frequentist statistics"
date = 2021-09-08

[taxonomies]
topics = ["Statistics", "MonteCarlo"]
+++


1. Suppose that you lived in a town with a population whose weights had a mean of 180 and a standard deviation of 9. 
Now, some people in this town underwent a weight reduction program, and you want to know if it had a significant effect. Did the "intervention" work?

![](/centrallimittheorem/1.png)




2. You should ask: what is the size of the sample that underwent the intervention? To understand why, let us
go back to the tosses of a fair coin that we talked about here: <https://twitter.com/rahuldave/status/1425883481821704192>.

![](/centrallimittheorem/2.png)




3. There, we increased the size of the sample of coins being tossed, and the fraction of heads, or the average of heads(1) and tails(0) got closer to 0.5 as the size N increased. We'd asked how fast does this fraction converge to 0.5?




4. This question is answered by the Central Limit Theorem (CLT), which, as it turns out, can also be used to answer the question about
the significance of the intervention! The CLT starts by recognizing that different samples of the same size N will have slightly different means.




5. The CLT says that these "sample means" follow a Normal Distribution whose standard
deviation decreases with increasing N. This standard deviation of sample means is called the **standard error**, and it is smaller than the underlying standard deviation σ of coin tosses.

![](/centrallimittheorem/5.png)




6. For example, if I take 1000 samples of size 500 each, the 100 means of the coin tosses distribute themselves according to the figure on the left. If I increase the size to 1000 tosses in a sample, we get the tighter distribution on the right.

![](/centrallimittheorem/6.png)




7. I talked about distributions in a previous thread: <https://twitter.com/rahuldave/status/1428458696481247233>. That thread describes the terms we use when we talk about distributions. Here, we are talking about the Gaussian or the Normal Distribution, which occurs everywhere in nature.




8. The Normal distribution N(µ, s) is symmetric about its mean µ, and 95% of the area of the distribution is between µ - 2s and µ + 2s. Lower s means smaller width; and the distribution becomes taller to compensate (keep the area at 1).

![](/centrallimittheorem/8.png)




9. As we increase the sample size N, the distributions of sample means tighten (left image). You can see more blue dots closer in to the 0.5 value as N increases to 1000. We plot the mean µ of these sample means in the figure on the right. µ gets closer to 0.5 too.

![](/centrallimittheorem/9.png)




10. Now let us compute the standard error (standard deviation of sample means from µ), at any N. The CLT tells us that this width s decreases with N as 1/√N. We can now use this formula to answer the question about the weight reduction intervention.

![](/centrallimittheorem/10.png)




11. The population's weights have a mean of 180 and a standard deviation of 9. Say you have a sample of 100 people in your intervention program. Then s = 9/√100 = 9/10 = 0.9. A set of samples of size 100 would have a mean of sample means of 180 and a standard error of 0.9. Tight!




12. Now, if your intervention sample of size 100 had a mean weight of 175, that number is 5 standard errors from the population mean, and thus very unlikely to have come from a sample drawn from the population. What if you had chosen a sample of 9 people instead?

![](/centrallimittheorem/12.png)




13. Then s = 9/√9 = 9/3 = 3. Now, if your intervention sample of size 9 had a mean weight of 175, this is less than 2 standard errors out from the population mean, and you cannot claim with a sample size of 9 that your intervention sample actually had a significant effect.

![](/centrallimittheorem/13.png)




14. Thus the CLT tells us the sample sizes we need to see significant effects! We'll talk more fun stuff, estimating Pi and its error with the LLN and CLT in future tweet threads. Follow me on twitter at @rahuldave and keep an eye on <https://stories.univ.ai> for more threads!




15. You can access a permalink to this thread here: <https://stories.univ.ai/centrallimittheorem/>. If you enjoy tweet threads like these and like to learn Data Science and AI, check out the courses we teach at <https://stories.univ.ai/aboutunivai/> or read this thread: LINK.

