from knowledge.models import ComputingFoundations
from core.models import SoftwareEngineering
from curriculum.models import CoreProfessionalContent


def main():
    """
    Test to execute some scripts.
    """

    knowledge = ComputingFoundations()
    print(knowledge.title)

    topic = knowledge.get_topic(knowledge.PROBLEM_SOLVING_TECHNIQUES)
    print(topic.title)

    subtopic = topic.get_subtopic(topic.DEFINITION_OF_PROBLEM_SOLVING)
    print(subtopic.title)
    print(subtopic.description)

    software = SoftwareEngineering()
    print(software.description)

    core = CoreProfessionalContent()
    print(core.title)
    print(core.description)
    print(core.knowledges)


if __name__ == "__main__":
    main()
