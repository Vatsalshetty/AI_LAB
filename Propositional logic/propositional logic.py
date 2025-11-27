import itertools

# Define propositional variables
variables = ['P', 'Q', 'R']

# Logical operations
def implies(a, b):
    return (not a) or b

def not_(a):
    return not a

def or_(a, b):
    return a or b

# Evaluate KB sentences
def evaluate_kb_sentences(P, Q, R):
    s1 = implies(Q, P)       # Q → P
    s2 = implies(P, not_(Q)) # P → ¬Q
    s3 = or_(Q, R)           # Q ∨ R
    kb_true = s1 and s2 and s3
    return s1, s2, s3, kb_true

# Generate all models and print truth table
print(f"{'P':<6}{'Q':<6}{'R':<6}{'Q→P':<8}{'P→¬Q':<10}{'Q∨R':<8}{'KB True?':<10}")
print("-" * 54)

kb_true_models = []

for vals in itertools.product([True, False], repeat=3):
    P, Q, R = vals
    s1, s2, s3, kb_true = evaluate_kb_sentences(P, Q, R)
    if kb_true:
        kb_true_models.append({'P': P, 'Q': Q, 'R': R})
    print(f"{str(P):<6}{str(Q):<6}{str(R):<6}{str(s1):<8}{str(s2):<10}{str(s3):<8}{str(kb_true):<10}")

# Entailment checks
def entails(models, formula_fn):
    return all(formula_fn(model) for model in models)

# Define entailment formulas
def formula_R(model):
    return model['R']

def formula_R_implies_P(model):
    return implies(model['R'], model['P'])

def formula_Q_implies_R(model):
    return implies(model['Q'], model['R'])

# Print entailment results
print("\nEntailment Results:")
print("KB ⊨ R:", entails(kb_true_models, formula_R))
print("KB ⊨ R → P:", entails(kb_true_models, formula_R_implies_P))
print("KB ⊨ Q → R:", entails(kb_true_models, formula_Q_implies_R))