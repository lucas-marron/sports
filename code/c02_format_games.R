
library(arrow)

fp_root <- dirname(dirname(rstudioapi::getSourceEditorContext()$path))

df_games <- read_parquet(file.path(fp_root, 'data', 'raw', 'games.parquet'))