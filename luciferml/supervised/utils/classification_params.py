import numpy as np
parameters_svm_1 = [
    {'kernel': ['rbf'], 'gamma': [0.1, 0.5, 0.9, 1],
        'C': np.logspace(-4, 4, 5)},
]
parameters_svm_2 = [
    {'kernel': ['rbf'], 'gamma': [1e-4, 0.1, 0.3,
                                  0.5, 0.7, 0.9, 1], 'C': np.logspace(-4, 4, 10)},
    {'kernel': ['linear'], 'gamma': [1e-4, 0.1, 0.3,
                                     0.5, 0.7, 0.9, 1], 'C': np.logspace(-4, 4, 10)},
    {'kernel': ['poly'], 'gamma': [1e-4, 0.1, 0.3,
                                   0.5, 0.7, 0.9, 1], 'C': np.logspace(-4, 4, 10)},
]
parameters_svm_3 = [
    {'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 0.1, 0.2, 0.3, 0.4,
                                  0.5, 0.6, 0.7, 0.8, 0.9], 'C': np.logspace(-4, 4, 20)},
    {'kernel': ['linear'], 'gamma': [1e-3, 1e-4, 0.1, 0.2, 0.3,
                                     0.4, 0.5, 0.6, 0.7, 0.8, 0.9], 'C': np.logspace(-4, 4, 20)},
    {'kernel': ['poly'], 'gamma': [1e-3, 1e-4, 0.1, 0.2, 0.3,
                                   0.4, 0.5, 0.6, 0.7, 0.8, 0.9], 'C': np.logspace(-4, 4, 20)},
    {'kernel': ['sigmoid'], 'gamma': [1e-3, 1e-4, 0.1, 0.2, 0.3,
                                      0.4, 0.5, 0.6, 0.7, 0.8, 0.9], 'C': np.logspace(-4, 4, 20)},
]


parameters_knn_1 = [{
    'n_neighbors': list(range(0, 11)),
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'kd_tree', 'brute'],
}]
parameters_knn_2 = [{
    'n_neighbors': list(range(0, 21)),
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
    'n_jobs': [1, 0]
}]
parameters_knn_3 = [{
    'n_neighbors': list(range(0, 31)),
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
    'n_jobs': [1, 0]
}]

parameters_dt_1 = [{
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_depth': [4,  6,  8,  10,  12,  20,  40, 70],

}]
parameters_dt_2 = [{
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_features': [2, 3],
    'max_depth': [4, 6, 7,  9, 10, 12, 20,  40, 50, 90, 120],

}]
parameters_dt_3 = [{
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_features': [2, 3],
    'max_depth': [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 70, 90, 120, 150],

}]

parameters_rfc_1 = [{
    'criterion': ['gini', 'entropy'],
    'n_estimators': [100, 200, 300, 400, 500, 750, 1000],
    'max_depth': [4,  6,  8,  10,  12,  20,  40, 70],
    'max_features': [2, 3],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
}]
parameters_rfc_2 = [{
    'criterion': ['gini', 'entropy'],
    'n_estimators': [50, 100, 150, 200, 250, 300, 400, 500, 700, 900, 1000],
    'bootstrap': [True, False],
    'max_depth': [4, 6, 7,  9, 10, 12, 20,  40, 50, 90, 120],
    'max_features': [2, 3],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
}]
parameters_rfc_3 = [{
    'criterion': ['gini', 'entropy'],
    'n_estimators': [50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000],
    'bootstrap': [True, False],
    'max_depth': [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 70, 90, 120, 150],
    'max_features': [2, 3],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
}]

parameters_xgb_1 = [{
    'min_child_weight': [1, 5, 10],
    'gamma': [0.1, 0.5, 0.9, 1],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'max_depth': [4,  6,  8,  10,  12,  20,  40, 70],
    'learning_rate': [0.3, 0.1],
}]
parameters_xgb_2 = [{
    'min_child_weight': [1, 5, 10],
    'gamma': [1e-3, 1e-4, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'max_depth': [4, 6, 7,  9, 10, 12, 20,  40, 50, 90, 120],
    'learning_rate': [0.3, 0.1, 0.01],
}]
parameters_xgb_3 = [{
    'min_child_weight': [1, 5, 10],
    'gamma': [1e-4, 0.1, 0.3,
              0.5, 0.7, 0.9, 1],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'max_depth': [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 30, 40, 50, 70, 90, 120, 150],
    'learning_rate': [0.3, 0.1, 0.03],
}]

parameters_ann_1 = [{'batch_size': [20, 50, 32],
                   'nb_epoch': [200, 100, 300],
                   'input_units': [5, 6, 10,],

                   }]
parameters_ann_2 = [{'batch_size': [ 20, 50, 25, 32],
                  'nb_epoch': [200, 100, 300, 350],
                   'input_units': [5, 6, 10, 11, 12,],

                   }]
parameters_ann_3 = [{'batch_size': [100, 20, 50, 25, 32],
                   'nb_epoch': [200, 100, 300, 400],
                   'input_units': [5, 6, 10, 11, 12, 15],

                   }]   

parameters_lin_1 = [{
    'penalty': ['l1', 'l2', ],
    'solver': ['newton-cg', 'liblinear', ],
    'C': np.logspace(-4, 4, 5),
}]
parameters_lin_2 = [{
    'penalty': ['l1', 'l2', 'elasticnet',],
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    'C': np.logspace(-4, 4, 15),
}]
parameters_lin_3 = [{
    'penalty': ['l1', 'l2', 'elasticnet', ],
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    'C': np.logspace(-4, 4, 20),
}]
