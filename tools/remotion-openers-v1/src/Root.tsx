import { Composition } from "remotion";
import { OpenerCSF, OpenerAI, OpenerCase, OpenerLab } from "./Openers";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition id="OpenerCSF" component={OpenerCSF} durationInFrames={440} fps={30} width={1920} height={1080} />
      <Composition id="OpenerAI" component={OpenerAI} durationInFrames={400} fps={30} width={1920} height={1080} />
      <Composition id="OpenerCase" component={OpenerCase} durationInFrames={450} fps={30} width={1920} height={1080} />
      <Composition id="OpenerLab" component={OpenerLab} durationInFrames={290} fps={30} width={1920} height={1080} />
    </>
  );
};
