# TeXSCII
Implementation of the [/r/dailyprogrammer challenge of the day](https://www.reddit.com/r/dailyprogrammer/comments/38nhgx/20150605_challenge_217_practical_exercise_texscii/) in whatever language I decide to use.

This converts LaTeX equations into ASCII symbols that can be printed on the command line.

## Commands
- `\frac{top}{bottom}`: A fraction with the given top and bottom pieces
- `\sqrt{content}`: A square-root sign
- `\root{power}{content}`: A root sign with an arbitrary power (eg. cube-root, where the power 3 is at the top-left of the radical symbol)
- `_{sub}`: Subscript
- `^{sup}`: Superscript
- `_{sub}^{sup}`: Subscript and superscript (one on top of the other)
- `\pi`: Output the greek symbol for pi

## Usage
```sh
$ python TeXSCII.py < sample.txt 
# /r/dailyprogrammer test cases

      x   
log (e )=x
   e      



 3   5  3   
F  =2 *7 -30
 21         



   3 1   3 _
sin (-π)=-v3
     3   8  



       ______
      / 2    
  -b+v b -4ac
x=-----------
      2a     



    3________________________________________________                                                             
    /                  ______________________________                                                             
   /    3         2   /    2     3     3         2  2                             3_   2                          
  v  -2b +9abc-27a d+v 4(-b +3ac) +(-2b +9abc-27a d)    b                         v2(-b +3ac)                     
x=--------------------------------------------------- - -- - -----------------------------------------------------
                          3_                            3a       3________________________________________________
                         3v2a                                    /                  ______________________________
                                                                /    3         2   /    2     3     3         2  2
                                                             3av  -2b +9abc-27a d+v 4(-b +3ac) +(-2b +9abc-27a d) 


```

## License
[License](/LICENSE)