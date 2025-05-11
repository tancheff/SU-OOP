from typing import List

from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    ARTIFACT_TYPES = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact
    }

    COLLECTOR_TYPES = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }

    def __init__(self):
        self.artifacts: List[BaseArtifact] = []
        self.collectors: List[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float,
                          artifact_space: int) -> str:
        artifact: BaseArtifact = next(filter(lambda a: a.name == artifact_name, self.artifacts), None)

        if artifact_type not in self.ARTIFACT_TYPES:
            raise ValueError("Unknown artifact type!")

        if artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        self.artifacts.append(self.ARTIFACT_TYPES[artifact_type](artifact_name, artifact_price, artifact_space))
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str) -> str:
        collector: BaseCollector = next(filter(lambda c: c.name == collector_name, self.collectors), None)

        if collector_type not in self.COLLECTOR_TYPES:
            raise ValueError("Unknown collector type!")

        if collector:
            return f"{collector_name} has been already registered!"

        self.collectors.append(self.COLLECTOR_TYPES[collector_type](collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str) -> str:
        collector: BaseCollector = next(filter(lambda c: c.name == collector_name, self.collectors), None)
        artifact: BaseArtifact = next(filter(lambda a: a.name == artifact_name, self.artifacts), None)

        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str) -> str:
        artifact: BaseArtifact = next(filter(lambda a: a.name == artifact_name, self.artifacts), None)

        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float) -> str:
        count = len([c.increase_money() for c in self.collectors if c.available_money <= max_money])

        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        sorted_collectors = sorted(
            self.collectors, key=lambda collector: (
                -len(collector.purchased_artifacts),
                collector.name
            )
        )

        # връща многомерен масив (матрица)
        # всеки вложен масив съдържа артефактите на съответния колекционер
        # --> len([[artifact for artifact in collector.purchased_artifacts] for collector in self.collectors])

        sold_artifacts = len([artifact for collector in self.collectors for artifact in collector.purchased_artifacts])

        count_of_available_artifacts = len(self.artifacts)

        message = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sold_artifacts}",
            f"Available artifacts for sale: {count_of_available_artifacts}",
            "***",
            "\n".join([c.__str__() for c in sorted_collectors])
        ]

        return "\n".join(message)
