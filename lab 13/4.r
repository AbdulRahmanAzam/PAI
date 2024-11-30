calculate_tax <- function(income) {
  if (income < 30000) {
    tax <- 0
  } else if (income <= 70000) { # not need to write && < 30000
    tax <- 0.10 * income
  } else if (income <= 100000) { # because it is obv that it is below 30000
    tax <- 0.15 * income
  } else {
    tax <- 0.20 * income
  }
  return(tax)
}

income <- 85000
cat("Income:", income, "Tax:", calculate_tax(income), "\n")
