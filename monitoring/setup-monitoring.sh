echo "Installing required CRDs..."
kubectl apply -f https://github.com/prometheus-operator/prometheus-operator/releases/download/v0.70.0/bundle.yaml


echo "Waiting 15 seconds for CRDs to finish installing..."
sleep 15


helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update


helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set prometheus.service.type=LoadBalancer \
  --set grafana.service.type=LoadBalancer \
  --set grafana.adminPassword='admin123'

echo "Installation started. Use the commands below to get LoadBalancer IPs:"

echo ""
echo "Grafana:"
echo "kubectl get svc -n monitoring kube-prometheus-stack-grafana"
echo ""
echo "Prometheus:"
echo "kubectl get svc -n monitoring kube-prometheus-stack-prometheus"
