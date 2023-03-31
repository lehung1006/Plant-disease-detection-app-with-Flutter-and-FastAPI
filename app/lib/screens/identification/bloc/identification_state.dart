part of 'identification_bloc.dart';

@immutable
abstract class IdentificationState extends Equatable {
  const IdentificationState();

  @override
  List<Object> get props => [];
}

class IdentificationInitial extends IdentificationState {}

class GetClassifyResultSuccess extends IdentificationState {
  final Item item;

  const GetClassifyResultSuccess({required this.item});
}

class GetClassifyResultFailure extends IdentificationState {
  final Exception e;

  const GetClassifyResultFailure({required this.e});
}

class GetPestDetectionResultSuccess extends IdentificationState {
  final PestDetection pestDetection;

  const GetPestDetectionResultSuccess({required this.pestDetection});
}

class GetPestDetectionResultFailure extends IdentificationState {
  final Exception e;

  const GetPestDetectionResultFailure({required this.e});
}