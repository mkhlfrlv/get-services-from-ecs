from get_ecs_clusters import get_ecs_clusters_in_all_regions
from get_ecs_services import get_ecs_cluster_services
from get_service_variables import get_service_environment_variables


def get_vars_all_services():
    all_clusters = get_ecs_clusters_in_all_regions()
    all_services = get_ecs_cluster_services(all_clusters)

    for region, clusters in all_services.items():
        for cluster, services in clusters.items():
            # print(cluster, services)
            for service, _ in services.items():
                print(service, "\n")
                print(get_service_environment_variables(region, cluster, service))

        # for cluster in range(len(region)):
        #     print(region[cluster])
        #     # for service in cluster:
        #     #     print(service)


if __name__ == '__main__':
    get_vars_all_services()
