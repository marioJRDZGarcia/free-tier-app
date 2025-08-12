variable "project_name" {
  description = "Nombre del proyecto"
  type        = string
  default     = "free-tier-app"
}

variable "app_port" {
  description = "Puerto de la aplicación"
  type        = number
  default     = 8000
}

variable "db_username" {
  description = "Usuario de la base de datos"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "Contraseña de la base de datos"
  type        = string
  sensitive   = true
}

variable "github_repo" {
  description = "Repositorio de GitHub (usuario/repo)"
  type        = string
  default     = "marioJRDZGarcia/free-tier-app"
}