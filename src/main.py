from data_loader import load_datasets
from model import build_model
from trainer import train_model
from tuner import tune_model
from evaluate import evaluate_model
from plots import plot_history, plot_confusion_matrix

# Load datasets
train_ds, val_ds, test_ds, class_names = load_datasets("fish")

print("\nClasses:")
print(class_names)

# Build CNN
model = build_model(
    len(class_names)
)

model.summary()

# Train baseline model
history = train_model(
    model,
    train_ds,
    val_ds,
    epochs=20
)

#Hyperparameter Search
print("\nStarting Hyperparameter Search...\n")

best_model, tuned_history, best_hp = tune_model(

    train_ds,

    val_ds,

    len(class_names)

)

#Evaluate model
print("\nEvaluating Baseline Model...\n")

baseline_metrics = evaluate_model(
    model,
    test_ds
)

print("\nEvaluating Tuned Model...\n")

tuned_metrics = evaluate_model(
    best_model,
    test_ds
)

#Plots
plot_history(
    history,
    "baseline",
    "Baseline CNN"
)

plot_history(
    tuned_history,
    "optimized",
    "Optimized CNN"
)

plot_confusion_matrix(
    baseline_metrics["matrix"],
    class_names,
    "baseline_confusion_matrix"
)

plot_confusion_matrix(
    tuned_metrics["matrix"],
    class_names,
    "optimized_confusion_matrix"
)