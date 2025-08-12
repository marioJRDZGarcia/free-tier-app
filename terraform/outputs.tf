output "ecs_cluster_name" {
  value = aws_ecs_cluster.cluster.name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}

output "rds_endpoint" {
  value = aws_db_instance.database.endpoint
}