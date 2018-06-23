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

    topic = knowledge.get_topic(knowledge.BASIC_USER_HUMAN_FACTORS)
    print(topic.title)

    subtopic = topic.get_subtopic(topic.USER_INPUT_AND_OUTPUT)
    print(subtopic.title)
    print(subtopic.description)


if __name__ == "__main__":
    main()
