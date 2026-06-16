<h2><a href="https://leetcode.com/problems/merge-strings-alternately/">1768. Merge Strings Alternately</a></h2><h3>Easy</h3><hr><p>You are given two strings <code>word1</code> and <code>word2</code>. Merge them by taking characters in alternating order, starting with <code>word1</code>.</p>

<p>If one string still has characters left after the other string ends, append the remaining characters to the merged string.</p>

<p>Return the merged string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = "abc", word2 = "pqr"
<strong>Output:</strong> "apbqcr"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = "ab", word2 = "pqrs"
<strong>Output:</strong> "apbqrs"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = "abcd", word2 = "pq"
<strong>Output:</strong> "apbqcd"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>
