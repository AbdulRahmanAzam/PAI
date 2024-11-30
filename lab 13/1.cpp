calculate_grade <- function(score){
    if(score >= 90){
        grade <- "A"
    }else if(score >= 80){
        grade <- "B"
    }else if(score >= 70){
        grade <- "C"
    }else {
        grade <- "Fail"
    }
    return(grade)
}

score <- 85
cat("Percentage: ", score, " Grade: ", calculate_grade(score))
