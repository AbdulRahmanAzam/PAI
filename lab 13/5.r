### ALL THE COMMENTS WERE WRITTEN BY CHATGPT FOR BETTER UNDERSTANDING LATER ###


# Load necessary libraries
library(tm)            # Text mining
library(e1071)         # For Naive Bayes
library(caret)         # For evaluation metrics

# 1. Load the dataset
data <- read.csv("spam.csv", stringsAsFactors = FALSE, encoding = "latin1")
data <- data[, c("v1", "v2")]  # Keep only the relevant columns
colnames(data) <- c("label", "message")  # Rename columns
data$label <- as.factor(ifelse(data$label == "spam", 1, 0))  # Encode labels (spam = 1, ham = 0)

# 2. Preprocess the text
corpus <- Corpus(VectorSource(data$message))
corpus <- tm_map(corpus, content_transformer(tolower))  # Convert to lowercase
corpus <- tm_map(corpus, removePunctuation)            # Remove punctuation
corpus <- tm_map(corpus, removeNumbers)                # Remove numbers
corpus <- tm_map(corpus, removeWords, stopwords("english"))  # Remove stopwords
dtm <- DocumentTermMatrix(corpus)                      # Convert to term-document matrix
dtm <- removeSparseTerms(dtm, 0.99)                    # Remove sparse terms

# 3. Split data into training and testing sets
set.seed(42)
train_indices <- sample(1:nrow(data), 0.7 * nrow(data))  # 70% for training
train_dtm <- dtm[train_indices, ]
test_dtm <- dtm[-train_indices, ]
train_labels <- data$label[train_indices]
test_labels <- data$label[-train_indices]

# 4. Train a Multinomial Naive Bayes Classifier
model <- naiveBayes(as.matrix(train_dtm), train_labels)

# 5. Predict on the test set
predictions <- predict(model, as.matrix(test_dtm))

# 6. Evaluate the Model
conf_matrix <- confusionMatrix(predictions, test_labels)
print(conf_matrix)

# Accuracy
cat("Accuracy: ", conf_matrix$overall["Accuracy"], "\n")
