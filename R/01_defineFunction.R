my_fun <- function(arg1, arg2){
  body
}


Example
add <- function(x, y=1) {
  x+y
}

###########################
3 components to functions
###########################
1. formals argument(add)
$x

$y
[1] 1

2. body(add)
{
  x+y
}

3. environment(add)
<environment: R_GlobalEnv>

###################
Return value: below code returns absolute value
###################
f <- function(x) {
  if (x < 0) {
    -x
  } else  {
    x
  }
}

Functions can be treated as regular objects
