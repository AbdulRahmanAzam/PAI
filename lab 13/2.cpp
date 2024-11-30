sumOfEven <- function(num) {
  even <- num[num %% 2 == 0]
  return(sum(even))
}

num <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cat("Sum of even numbers:", sumOfEven(num), "\n")
