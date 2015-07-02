# MeCab's Python 2 binding has a bug

This code (whose encoding is utf-8),

```
import MeCab

node = MeCab.Tagger().parseToNode("あいうえお")
x = node.feature
```

causes core dump. This can be because the node generated by the tagger
accesses to its object which is already freed up.

To deal with the problem, change the code above like the below.

```
import MeCab

tagger = MeCab.Tagger()
node = tagger.parseToNode("あいうえお")
x = node.feature
```