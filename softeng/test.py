# from core.models import SoftwareEngineering
# from curriculum.models import CoreProfessionalContent
from knowledge.models import ComputingFoundations


def main():
    """
    Test to execute some scripts.
    """

    # software = SoftwareEngineering()
    # print(software.description)

    # core = CoreProfessionalContent()
    # print(core.title)
    # print(core.description)
    # print(core.knowledges)

    knowledge = ComputingFoundations()
    print(knowledge.title)
    print(knowledge.curriculum)

    topic = knowledge.get_topic(knowledge.ALGORITHMS_AND_COMPLEXITY)
    print("TITLE: " + topic.title)
    # print("DESCRIPTION: " + topic.description)

    subtopic = topic.get_subtopic(topic.OVERVIEW_OF_ALGORITHMS)
    print("TITLE: " + subtopic.title)
    print("DESCRIPTION: " + subtopic.description)


if __name__ == "__main__":
    main()
