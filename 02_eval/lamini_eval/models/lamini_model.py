from lamini_prompt.lamini_model_stage import LaminiModelStage


def load_lamini_model(args):
    return LaminiModel()


class LaminiModel:
    def get_stages(self, dataset):
        return [LaminiModelStage(dataset)]
