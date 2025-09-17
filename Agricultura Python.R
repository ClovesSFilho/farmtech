# Ler o CSV
dados <- read.csv("C:/Users/clove/Documents/insumos.csv", sep = ",", dec = ".", header = TRUE)

# Visualizar
print(dados)

# Média e desvio padrão de qtd_por_metro
media_qtd <- mean(dados$qtd_por_metro)
desvio_qtd <- sd(dados$qtd_por_metro)

# Total geral
total_geral <- sum(dados$total)

cat("Média da qtd_por_metro:", media_qtd, "\n")
cat("Desvio padrão da qtd_por_metro:", desvio_qtd, "\n")
cat("Total geral de insumos:", total_geral, "\n")
